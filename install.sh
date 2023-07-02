#!/bin/bash

function dotfiles {
  /usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME $@
}

git clone --bare https://github.com/GeorgiKarapetrov/dotfiles.git $HOME/.dotfiles
mkdir -p $HOME/.dotfiles-backup
dotfiles checkout master /
if [ $? = 0 ]; then
  echo "Checked out dotfiles.";
  else
    echo "Backing up pre-existing dot files.";
    dotfiles checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | xargs -I{} mv {} $HOME/.dotfiles-backup/{}
fi;
dotfiles checkout master /
dotfiles config status.showUntrackedFiles no

echo yay_init
echo sudo systemctl enable preload
echo sudo rm /etc/systemd/system/display-manager.service
echo sudo systemctl enable lightdm
# echo sudo groupadd fuse
# echo sudo usermod -a -G fuse georgi
