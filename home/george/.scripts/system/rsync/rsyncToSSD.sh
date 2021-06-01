#!/bin/bash
#sudo mount /dev/sdb1 ~/a
#sudo mkdir /run/media/george/0a5e3c18-6a12-42d2-98e8-9d7bd0f4df6e/
#sudo mount /dev/sdb1 /run/media/george/0a5e3c18-6a12-42d2-98e8-9d7bd0f4df6e/

#build a list of installed (or removed) packages
yay -Qqe > pkglist.txt #manjaro

sudo rsync -avhP --delete-excluded --delete-after --exclude="Downloads/torrent/" /home/george /run/media/george/78b44673-a8c9-4d9c-b4c9-690ec658925f/
rsync -r georgi.karapetrov.top/build/ pi@blacked:/var/www/georgi.karapetrov.top
#sudo dpkg --get-selections > ~/a/Settings/my-packages.txt #debian

#on reinstall, run
#pacman -S --needed - < pkglist.txt #manjaro
#sudo dpkg --set-selections < ~/a/my-packages.txt # debian
#sudo apt-get -u dselect-upgrade

#sudo umount /dev/sdb1
#sudo rm -rf /run/media/george/0a5e3c18-6a12-42d2-98e8-9d7bd0f4df6e/

#To synchronize my samba source trees I use the following Makefile targets:
#
#           get:
#                   rsync -av --delete-excluded --delete-afteruzb --exclude '*~' samba:samba/ .
#           put:
#                   rsync -Cavuzb . samba:samba/
#           sync: get put
