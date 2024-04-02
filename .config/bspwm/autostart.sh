#!/bin/bash

function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

$HOME/.config/polybar/launch.sh &

xsetroot -cursor_name left_ptr &

# https://github.com/baskerville/sxhkd/issues/188#issuecomment-873682322
# use localectl in favor of setxkbmap; runs once; creates /etc/X11/xorg.conf.d/00-keyboard.conf
# localectl --no-convert set-x11-keymap us,bg pc105 ,phonetic grp:alt_caps_toggle
# setxkbmap -model pc105 -layout us,bg -variant ,phonetic -option grp:alt_caps_toggle
run gxkb &

run sxhkd -c ~/.config/bspwm/sxhkd/sxhkdrc && sleep 1 &

run conky -c $HOME/.config/bspwm/system-overview &
run nm-applet &
run pamac-tray &
run xfce4-power-manager &
numlockx on &
blueberry-tray &
picom --config $HOME/.config/bspwm/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
run volumeicon &
nitrogen --restore &

#custom
pulseaudio-equalizer enable &
run /usr/lib/kdeconnectd &
run /usr/bin/kdeconnect-indicator &
run tixati &
run discord &
run telegram-desktop &
run alacritty &
if ! pgrep -f google-chrome ;
  then
	  (sleep 9 && run google-chrome-stable) &
fi
#qt apps QT_FONT_DPI=150, no longer needed due to /etc/profile.d/qt-hidpi.sh
# contents:
# export QT_DEVICE_PIXEL_RATIO=2
# chmod +x /etc/profile.d/qt-hidpi.sh
run keepassxc & #-style=gtk2
run flameshot & #-style=gtk2
run xfce4-power-manager &
# also in cron
mount | grep "${HOME}/Documents/gdrive" >/dev/null || google-drive-ocamlfuse -label home "${HOME}/Documents/gdrive"
(sleep 10 && run evolution) &
