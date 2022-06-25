#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#Find out your monitor name with xrandr or arandr (save and you get this line)
xrandr --output DisplayPort-0 --off --output DisplayPort-1 --off --output HDMI-A-0 --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-A-1 --mode 3840x2160 --rate 30 --pos 1920x0 --rotate normal --output DVI-D-0 --off
#xrandr --output VGA-1 --primary --mode 1360x768 --pos 0x0 --rotate normal
#xrandr --output DP2 --primary --mode 1920x1080 --rate 60.00 --output LVDS1 --off &
#xrandr --output LVDS1 --mode 1366x768 --output DP3 --mode 1920x1080 --right-of LVDS1
#xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off

$HOME/.config/polybar/launch.sh &

#change your keyboard if you need it
run setxkbmap -model pc105 -layout us,bg -variant ,phonetic -option grp:alt_caps_toggle
sleep 1; run gxkb &

#Some ways to set your wallpaper besides variety or nitrogen
#feh --bg-scale ~/.config/bspwm/wall.png &
#feh --bg-fill /usr/share/backgrounds/arcolinux/arco-wallpaper.jpg &
#feh --randomize --bg-fill ~/Képek/*
#feh --randomize --bg-fill ~/Dropbox/Apps/Desktoppr/*

dex $HOME/.config/autostart/arcolinux-welcome-app.desktop
xsetroot -cursor_name left_ptr &
run sxhkd -c ~/.config/bspwm/sxhkd/sxhkdrc &

run conky -c $HOME/.config/bspwm/system-overview &
#run variety &
run nm-applet &
run pamac-tray &
run xfce4-power-manager &
numlockx on &
blueberry-tray &
picom --config $HOME/.config/bspwm/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
run volumeicon &
run thunderbird &
#nitrogen --restore &
run caffeine -a &

#custom
sleep 1; pulseaudio-equalizer enable &
run /usr/lib/kdeconnectd &
run /usr/bin/kdeconnect-indicator &
# wifi hotspot
#exec --no-startup-id bash $HOME/.scripts/create_ap.sh &
run tixati &
run terminator &
run firefox &
#qt apps QT_FONT_DPI=150, no longer needed due to /etc/profile.d/qt-hidpi.sh
# contents:
# export QT_DEVICE_PIXEL_RATIO=2
# chmod +x /etc/profile.d/qt-hidpi.sh
run keepassxc & #-style=gtk2
run flameshot & #-style=gtk2
run xfce4-power-manager &
run sleep 10; bspc desktop -f "^6" &
mount | grep "${HOME}/Documents/cloud/gdrive" >/dev/null || /usr/bin/google-drive-ocamlfuse "${HOME}/Documents/cloud/gdrive"
mountpoint -q $HOME/Documents/cloud/nextcloud || mount $HOME/Documents/cloud/nextcloud
