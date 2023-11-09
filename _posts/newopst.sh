#!/bin/bash

if [[ $# -ne 2 ]]; then
    echo 'need filename and post title'
    exit 1
fi

title=$2
filename="$(dirname "$(realpath "$0")")"/$(date '+%Y-%m-%d-')${1// /-}.md

echo $filename


cat << EOF > $filename
---
title: $title
date: $(date '+%Y-%m-%d %H:%M:%S')
img_path: /_posts/
math: true
---

EOF

