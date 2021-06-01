#!/bin/bash
sudo mount /dev/sda1 /mnt
rsync -rvP Documents/georgi.karapetrov.top/build pi@192.168.88.3:/home/pi/
sudo umount /mnt