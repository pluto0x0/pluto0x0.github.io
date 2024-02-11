---
title: 一次Linux迁移的记录
categories: Linux 
tags: Linux 
---

> 笔记本有一个2280和一个2240硬盘位，因此要把原来2280的盘迁移到2240的上。
{: .prompt-info }

硬盘上只有两个分区：UEFI引导分区（FAT32）和 `/` 挂载点（EXT4），因此迁移就比较容易

## 步骤

具体来说，

1. 同时挂载原硬盘和新硬盘，我这次是在原硬盘上的系统里挂载了新硬盘在`/mnt/`，并非使用live CD等，不过原理大同小异。
   这里原硬盘是`/dev/nvme1n1`，新硬盘是`/dev/nvme0n1`

2. 分区。使用了图形化的`gparted`，仿照原硬盘在新硬盘上分出300MB的UEFI引导分区`/dev/nvme0n1p1`和剩余的 `/` 挂载点`/dev/nvme0n1p3`，注意要把引导区的`boot`标志勾选。
   ![忽略swap](https://s2.loli.net/2023/10/29/gsdNaP2FreuOxLB.png)
   ![image.png](https://s2.loli.net/2023/10/29/nXyuU9xJRLcfpe8.png)

3. 复制原硬盘的 `/` 到新硬盘的 `/` 挂载点`/dev/nvme0n1p3`，注意要忽略：
	```shell
    '/dev/*','/proc/*','/sys/*','/tmp/*','/run/*','/mnt/*','/lost+found/*','/media/*'
    ```

    这些文件。
    我用的是`rsync`，具体命令见后面脚本。`dd`等命令更底层，还要涉及到文件系统resize的问题，`rsync`就不会。

5. 挂载 `/dev` `/sys/` ... 等关键目录，否则无法进入新系统。这相当于新硬盘的系统和老硬盘的系统公用这些路径，为后面chroot准备。
	```shell
	mount --bind /dev/ /mnt/dev/
	mount --bind /sys/ /mnt/sys/
	# 具体命令见后面脚本。
	```
	同时也要挂载新硬盘的引导分区到新硬盘的`/boot/efi`，从而能安装grub引导。
	```shell
	mount /dev/nvme0n1p1 /mnt/boot/efi
	```
6. 进入chroot环境。
	chroot就是更改当前Linux的root目录，此时相当于在新硬盘的系统中执行命令。
	```shell
	chroot /mnt
	```
6. 修改`/etc/fstab`里的UUID为当前新盘的UUID。grub是靠UUID找对应的盘的，这也是全盘克隆无法启动的原因，因为两个盘的UUID不一样。

	```shell
	blkid /dev/nvme0n1p3 # 查看UUID
	```

7. 修复grub引导
	```shell
	grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader=Manjaro --recheck
	```
	切记这是在chroot环境，因此路径是`/boot/efi`。
	最后写入grub

	```shell
	grub-update
	```
	在执行`grub-update`前可以安装`os-prober`，这样`grub-update`能检测所有硬盘中的引导区。当然现在电脑里有两个一样的Linux，需要把老的硬盘卸载、插入新的硬盘（比如win10）的，再进入新的Linux安装一遍`os-prober`后执行`grub-update`。

现在新的Linux就好了。

## grub2

grub2可以安装主题进行美化，我用的是[Gorgeous-GRUB](https://github.com/jacksaur/Gorgeous-GRUB)里挑选的[Virtuaverse](https://github.com/Patato777/dotfiles/tree/main/grub)，执行安装脚本即可。

## 自动脚本

脚本对于单个或多个挂载点的情况可以处理，至于有逻辑分区等等复杂的情况不知道行不行。

```shell
#!/bin/bash

# Regular Colors
BLACK='\033[0;30m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'

# Bold Colors (加粗)
BBLACK='\033[1;30m'
BRED='\033[1;31m'
BGREEN='\033[1;32m'
BYELLOW='\033[1;33m'
BBLUE='\033[1;34m'
BPURPLE='\033[1;35m'
BCYAN='\033[1;36m'
BWHITE='\033[1;37m'

# Underlined Colors (下划线)
UBLACK='\033[4;30m'
URED='\033[4;31m'
UGREEN='\033[4;32m'
UYELLOW='\033[4;33m'
UBLUE='\033[4;34m'
UPURPLE='\033[4;35m'
UCYAN='\033[4;36m'
UWHITE='\033[4;37m'

# Background Colors (背景色)
BG_BLACK='\033[40m'
BG_RED='\033[41m'
BG_GREEN='\033[42m'
BG_YELLOW='\033[43m'
BG_BLUE='\033[44m'
BG_PURPLE='\033[45m'
BG_CYAN='\033[46m'
BG_WHITE='\033[47m'

# No Color
NC='\033[0m'

# ===========================


efi_mnt=/boot/efi	# constant
mnt=/mnt/targetOS	# constant
mnt_source=/mnt/sourceOS	# constant

efi=0
declare -a from
declare -a to
declare -a point

ischroot=0

function error() {
	echo -e  "${BRED}ERROR: $1\nSee '--help'${NC} "
	exit 1
}

if [ "$UID" -ne 0 ]; then
	error "This script must be run as root."
	exit 1
fi

function color_echo() {
	local input="$1"
	# Replace words with colored words
	for colori in "${!from[@]}"; do
		input="${input//${from[colori]}/${BRED}${from[colori]}${NC}}"
		input="${input//${to[colori]}/${BGREEN}${to[colori]}${NC}}"
		# input="${input//${point[$i]}/${BCYAN}${point[$i]}${NC}}"
	done
	input="${input//${efi}/${BBLUE}${efi}${NC}}"
	input="${input//${mnt}/${BYELLOW}${mnt}${NC}}"
	input="${input//${mnt_source}/${BPURPLE}${mnt_source}${NC}}"
	input="${input//${efi_mnt}/${BCYAN}${efi_mnt}${NC}}"
	echo -e -n "$input"
}

# read arguments
while [[ "$#" -gt 0 ]]; do
	case $1 in
		--chroot)
			ischroot=1
			shift 1
			;;
		--efi)
			efi="$2"
			shift 2
			;;
		--move)
			if [[ "$#" -le 3 ]]; then
				error "--move requires 3 arguments"
			fi
			point+=("$2")
			from+=("$3")
			to+=("$4")
			shift 4
			;;
		--help)
			echo sudo $0 --efi "{efi} [--move / {from} {to} [--move {point} {from} {to} [...]]]"
			echo
			echo "{efi} {from} {to} are partitions like /dev/nvme0n1"
			echo "{point} are mount points of the corresponding partition"
			echo "note that the first mount point given must be '/'"
			exit 0
			;;
		*)
			error "Unknown parameter passed: $1"
			;;
	esac
done

function run_cmd() {
	local cmd="$1"
	echo -n -e "${BCYAN} > ${NC}"
	color_echo "$2"
	echo -n -e " ${BG_WHITE}${UBLACK}[Y/n]${NC}:"
	read -r response < /dev/tty
	if [[ "$response" == "" \Vert  "$response" == "y" \Vert  "$response" == "y" ]]; then
		eval "$cmd"
	else
		if [ -z "$3" ]; then
			echo -e "${BRED}Command aborted.${NC}"
		else
			eval "$3"
		fi
	fi
}

get_uuid() {
	local device="$1"
	# Use blkid to fetch the UUID
	local uuid=$(blkid "$device" | sed -n 's/.* UUID="\([^"]*\)".*/\1/p')
	# Check if the UUID is empty
	if [[ -z "$uuid" ]]; then
		echo "No UUID found for device $device"
		return 1
	fi
	echo "$uuid"
}

if [[ ischroot -eq 0 ]]; then
	# check valid
	if [[ -z "$efi" ]]; then
		error "No EFI device assigned"
	fi
	if [ ${#from[@]} -eq 0 ]; then
		error "--move missing"
	fi
	if [[ ${point[0]} != "/" ]]; then
		error "First mouont point must be '/'"
	fi
	# output arguments
	color_echo "EFI partition: $efi\n"
	for i in "${!from[@]}"; do
		color_echo "Move from: ${from[$i]} (mount point ${BCYAN}${point[$i]}${NC}) to: ${to[$i]}\n"
	done
	# double check from uesr
	run_cmd "" "Continue?" "exit"

	mkdir -p $mnt 2> /dev/null
	mkdir -p $mnt_source 2> /dev/null

	for i in "${!from[@]}"; do
		run_cmd <<-EOF "
		mount ${to[$i]} ${mnt}
		mount ${from[$i]} ${mnt_source}
		" "Mounting ${to[$i]} to ${mnt}, ${from[$i]} to ${mnt_source}"
		EOF

		run_cmd <<-EOF "
		rm -rf $mnt/*
		" "Clearing $mnt (where ${to[$i]} is mounted)"
		EOF

		if [[ $i -eq 0 ]]; then
			run_cmd <<-EOF "
			rsync -aAX --stats $mnt_source/ $mnt/ --exclude={'/dev/*','/proc/*','/sys/*','/tmp/*','/run/*','/mnt/*','/lost+found/*','/media/*'}
			" "Copying from ${from[$i]} to $mnt (where ${to[$i]} is mounted) via rsync, with /dev/,/proc/,etc. excluded"
			EOF
		else
			echo $i iii
			run_cmd <<-EOF "
			rsync -aAX --stats $mnt_source/ $mnt/
			" "Copying from ${from[$i]} to $mnt (where ${to[$i]} is mounted) via rsync"
			EOF
		fi


		umount $mnt 2> /dev/null # always unmount
		umount $mnt_source 2> /dev/null # always unmount
	done

	run_cmd <<-EOF "
	for i in "\${!from[@]}"; do
		mkdir -p \${mnt}\${point[\$i]}
		mount \${to[\$i]} \${mnt}\${point[\$i]}
	done" "Mount all partitions to $mnt"
	EOF

	run_cmd <<-EOF "
	mount ${from[0]} $mnt_source
	for dir in /dev /dev/pts /proc /sys /sys/firmware/efi/efivars /run; do
		color_echo \"mounting $mnt_source\$dir to $mnt\$dir;\\n\"
		mount --bind $mnt_source\$dir $mnt\$dir
	done" "Mounting necessary points to $mnt from source OS"
	EOF

	run_cmd <<-EOF "
	mount $efi $mnt$efi_mnt
	" "Mounting EFI partition in $mnt$efi_mnt"
	EOF

	run_cmd <<-EOF "
	chroot $mnt /bin/bash $(realpath $0) --chroot $*
	" "Doing chroot (This will enter chroot environment)"
	EOF

	run_cmd <<-EOF "
	echo Press ENTER again to reboot!
	read
	reboot
	" "Ready to reboot"
	EOF

else
	echo "I am in chroot environment now!"
	old_uuid=$(get_uuid $from)
	uuid=$(get_uuid $to)
	color_echo "UUID of (from) $from is $old_uuid"
	echo
	color_echo "UUID of (to) $to is $uuid"
	echo

	run_cmd <<-EOF "
	sudo sed -i 's@$old_uuid@$uuid@g' /etc/fstab
	" "Now change UUID in /etc/fstab:\nreplace $old_uuid to $uuid"
	EOF

	run_cmd <<-EOF "
	grub-install --target=x86_64-efi --efi-directory=$efi_mnt --bootloader=Manjaro --recheck
	" "Intalling GRUB"
	EOF

	run_cmd <<-EOF "
	update-grub
	" "Updating GRUB"
	EOF

	run_cmd <<-EOF "
	exit
	" "exit chroot!"
	EOF

fi

echo "Quitting."
```

脚本还有待测试。
