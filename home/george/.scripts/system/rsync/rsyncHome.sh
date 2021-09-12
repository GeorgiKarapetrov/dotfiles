#!/bin/bash
yay -Qqe > /home/george/pkglist.txt
comm -23 <(pacman -Qqett | sort) <(pacman -Qqg base -g base-devel | sort | uniq) > .pkglist.test
sudo mount /dev/sda1 /mnt
sudo rsync -axHAXS --numeric-ids --info=progress2 --delete-excluded --delete-after --exclude="Downloads/torrent/" /home /mnt/
sudo umount /mnt
