#!/bin/bash
find -type f -exec echo {} \; -exec ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {} \;
echo "| grep -B1 3840x2160"
