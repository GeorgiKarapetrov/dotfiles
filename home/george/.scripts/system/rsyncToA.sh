#!/bin/bash
sudo mount /dev/sdc1 ~/a

#rsync
#note trailing slashes in source as well as dest

#docs
#sudo rsync -av --delete-excluded --delete-after ~/Desktop ~/a/
sudo rsync -av --delete-excluded --delete-after ~/Documents ~/a/

#media
#sudo rsync -av --delete-excluded --delete-after --exclude="torrent" --exclude="CF" --exclude="PR0N" ~/Downloads ~/a/
sudo mkdir ~/a/Video
sudo rsync -av --delete-excluded --delete-after ~/Videos/pol/ ~/a/Video/
sudo rsync -av --delete-excluded --delete-after ~/Music ~/a/
sudo rsync -av --delete-excluded --delete-after --exclude="Az/passport/naughty" ~/Pictures ~/a/

#settings
sudo rsync -av --delete-excluded --delete-after ~/dotfiles ~/a/


#package list
#build a list of installed (or removed) packages
pacaur -Qqe > pkglist.txt #manjaro
#sudo dpkg --get-selections > ~/a/Settings/my-packages.txt #debian

#on reinstall, run
#pacman -S --needed - < pkglist.txt #manjaro
#sudo dpkg --set-#selections < ~/a/my-packages.txt # debian
#sudo apt-get -u dselect-upgrade
#to start installing packages.

#sudo umount /dev/sdc1

#To synchronize my samba source trees I use the following Makefile targets:
#
#           get:
#                   rsync -av --delete-excluded --delete-afteruzb --exclude '*~' samba:samba/ .
#           put:
#                   rsync -Cavuzb . samba:samba/
#           sync: get put
