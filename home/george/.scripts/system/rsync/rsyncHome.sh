#!/bin/bash
yay -Qqe > /home/george/pkglist.txt
sudo mount /dev/sda1 /mnt
sudo rsync -axHAXS --numeric-ids --info=progress2 --delete-excluded --delete-after --exclude="Downloads/torrent/" /home /mnt/
sudo umount /mnt
