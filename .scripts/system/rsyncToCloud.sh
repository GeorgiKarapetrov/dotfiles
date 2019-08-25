#!/bin/bash
#do not sudo rsync; root has no write access on the destination
sudo mount /dev/sda7 ~/a

rsync -v ~/a/timeshift/2019-03-25_17-06-19.tar.gz /run/user/1000/gvfs/dav\:host\=kmu.files.cnow.at\,ssl\=true\,user\=strammr%40abv.bg\,prefix\=%2Fremote.php%2Fwebdav/

rsync -v ~/a/timeshift/2019-03-25_17-06-19.tar.gz /run/user/1000/gvfs/google-drive\:host\=gmail.com\,user\=g.d.karapetrov/

sudo umount /dev/dsa7

