
### Dotfiles
- clone to $HOME
- make install.sh and install_packages executable:
*chmod 755 install.sh && chmod 755 install_packages 755*
- run install scripts:
./install.sh && ./install_packages.sh

##### Issues:
- install.sh creates infinitely deep symlinks such as ~/.config/i3/i3/i3/i3....
- install_packages.sh hasn't been tested

