---
title: 记录一些实用的ffmpeg命令
---

## 转换flac

无损转换+保留封面

<!-- <https://paste.ubuntu.com/p/zvhdZgH4sk/> -->

```bash
for file in ./*.flac
do
	ffmpeg -i "$file" -c:v copy -c:a alac "${file%.*}.m4a"
done

```
