export QT_QPA_PLATFORMTHEME="qt5ct"
export EDITOR=/usr/bin/nvim
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"

# opam configuration
test -r /home/george/.opam/opam-init/init.sh && . /home/george/.opam/opam-init/init.sh > /dev/null 2> /dev/null || true
