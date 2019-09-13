#!/bin/bash
#https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks#Install_packages_from_a_list
sudo pacman -S pacaur
pacaur -S --needed < pkglist.txt

echo 'Install Graphics driver'
echo 'Add to bumblebee:'
echo 'systemctl enable bumblebeed'
echo 'gpasswod -a george bumblebee'
echo 'mount Downloads from /etc/fstab'
#must have:
#pacaur -S indicator-kdeconnect git pavucontrol rofi terminator guake firefox gxkb compton tixati vbetool font-awesome adobe-source-code-pro-fonts-2 pulseaudio-equalizer-ladspa nitrogen
