#!/bin/bash

yes |yay -S pass pass-otp keepassxc fzf linux-lts linux-zen qutebrowser sublime-text-dev terminator vifm vlc youtube-dl mpv rts_bpp-dkms-git
yes |yay -S npm yarn git-interactive-rebase-tool electrum monero monero-gui pulseaudio-equalizer-ladspa preload tixati gxkb neovim cherrytree kdeconnect gsimplecal cronie tldr firefox-extension-kdeconnect
yes| yay -Rns snapd gutenprint cups-pdf cups termite sddm-config-editor-git sddm
echo -e "Consider running\
\nyes |yay -S zathura zsh zsh-completions zsh-fast-syntax-highlighting zsh-syntax-highlighting"
