git clone --bare git@github.com:GeorgiKarapetrov/dotfiles.git $HOME/.dotfiles
function dotfiles {
   sudo /usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=/ $@
}
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

#yes |yay -S npm yarn git-interactive-rebase-tool electrum monero monero-gui pulseaudio-equalizer-ladspa preload tixati gxkb neovim cherrytree kdeconnect gsimplecal
#yes| yay -Rns snapd gutenprint cups-pdf cups termite sddm-config-editor-git sddm\n
#sudo systemctl enable preload
#sudo rm /etc/systemd/system/display-manager.service
#sudo systemctl enable lightdm
#sudo groupadd fuse
#sudo usermod -a -G fuse george
