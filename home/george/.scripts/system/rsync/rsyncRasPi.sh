#!/bin/bash
sudo mount /dev/sda1 /mnt
sudo rsync -axHAXS --numeric-ids --info=progress2 pi@192.168.88.3:/home/pi /mnt/rasPi/
sudo rsync -axHAXS --numeric-ids --info=progress2 pi@192.168.88.3:/etc /mnt/rasPi
sudo rsync -axHAXS --numeric-ids --info=progress2 pi@192.168.88.3:/var/www /mnt/rasPi
sudo umount /mnt