#!/bin/bash
sudo rsync -rv --ignore-existing ~/Desktop /media/george/android/Desktop && \
sudo rsync -rv --ignore-existing --exclude="git" --exclude='Non-math/knigi/peterson' ~/Documents /media/george/android/Documents && \
sudo rsync -rv --ignore-existing ~/Media/Videos/pol /media/george/android/Media/Video && \
sudo rsync -rv --ignore-existing ~/Media/Music /media/george/android/Media/Music && \
sudo rsync -rv --ignore-existing --exclude="Bush+PeachLips" --exclude="Sets" ~/Media/Pictures /media/george/android/Media/Pictures && \
\
sudo rsync -rv --ignore-existing ~/.spacemacs /media/george/android/Settings/.spacemacs && \
sudo rsync -rv --ignore-existing ~/.emacs.d/init.el /media/george/android/Settings/.emacs.d/init.el && \
sudo rsync -rv --ignore-existing ~/.config /media/george/android/Settings/.config && \
sudo rsync -rv --ignore-existing ~/.local --exclude="lib" /media/george/android/Settings/.local && \
sudo rsync -rv --ignore-existing ~/.moziilla /media/george/android/Settings/.mozilla && \
sudo rsync -rv --ignore-existing ~/.bashrc /media/george/android/Settings/.bashrc && \
sudo rsync -rv --ignore-existing ~/.bash_profile /media/george/android/Settings/.bash_profile && \
sudo rsync -rv --ignore-existing ~/.bash_histoy /media/george/android/Settings/.bash_histoy && \
sudo rsync -rv --ignore-existing ~/.profile /media/george/android/Settings/.profile && \
\
sudo rsync -rv --ignore-existing --exclude="cache" --exclude="lib" /var/ /media/george/android/Settings/var && \
sudo rsync -rv --ignore-existing /etc /media/george/android/Settings/etc

