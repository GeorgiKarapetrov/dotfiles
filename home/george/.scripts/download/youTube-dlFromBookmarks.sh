#!/bin/bash
# Script exports bookmarks from Google Chrome, donwload liks with youtube-dl and convert them to mp3 

 for binary in google-chrome youtube-dl ffmpeg; do
    type -P "$binary" &>/dev/null
    [ "$?" != 0 ] && echo -e "\n'$binary' required but not found, exiting!\n" && exit 1
 done

 cat ~/.config/google-chrome/Default/Bookmarks | grep youtube | cut -d ":" -f2-3 | cut -d '"' -f2 > bookmarks.txt

 if  [ ! -s bookmarks.txt ]; then
    echo -e "\nFile bookmarks.txt not found or is empty, exiting!\n" && exit 1
 fi

 for line in $(cat bookmarks.txt); do 
    youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 --output "%(title)s.%(ext)s" "$line" &
    sleep 2 
 done

 
 exit 0
