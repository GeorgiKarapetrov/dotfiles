#!/bin/bash
for i in *.mp4; do 
    ffmpeg -i "$i" -vn -acodec copy "$i".aac; 
done
