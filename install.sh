#!/bin/bash

function dotfiles {
  /usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME $@
}

git clone --bare git@github.com:GeorgiKarapetrov/dotfiles.git $HOME/.dotfiles
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

#yes |yay -S npm yarn git-interactive-rebase-tool electrum monero monero-gui pulseaudio-equalizer-ladspa preload tixati gxkb neovim cherrytree kdeconnect gsimplecal cronie tldr firefox-extension-kdeconnect rts_bpp-dkms-git pastebinit davfs2 google-drive-ocamlfuse
#yes| yay -Rns snapd gutenprint cups-pdf cups termite sddm-config-editor-git sddm\n
#sudo systemctl enable preload
#sudo rm /etc/systemd/system/display-manager.service
#sudo systemctl enable lightdm
#sudo groupadd fuse
#sudo usermod -a -G fuse georgi
#text editors:
#yay -S sublime-text-3 notepadqq bluefish brackets-bin atom
#yay -S vscodium codelobster uex
#dummy
