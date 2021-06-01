

# This script should only run when X is running.
# Exit immediately if X isn't running.
pgrep X > /dev/null || exit 0

# Here we assign the desktops we want to move to an array
# so that we can address them more easily.
# POSIX shell doesn't have really arrays so we use parameters
# as a makeshift array:
set -- "$(bspc query --desktops | tail -n 2 | sed -n 1p)" "$(bspc query --desktops | tail -n 2 | sed -n 2p)"

# This is just a function that restarts the panel.
# Nothing fancy here.
reset_panel() {
    pkill -x panel
    setsid panel &
}

BSPWM_EXTERNALMONITOR="HDMI-A-0"
BSPWM_INTERNALMONITOR="HDMI-A-1"

# This is the function for when an external monitor is connected
monitor_add() {
    # Before the monitor gets recognized, of course we have to turn it on first.
    # I always have my monitor on the right side of the laptop screen so I don't
    # bother with scripting other positions here, but you could add an if or case
    # statement if you want to have some flexibility.
    xrandr --output "$BSPWM_EXTERNALMONITOR" --left-of "$BSPWM_INTERNALMONITOR" --auto
    # Then, we move a desktop to the monitor we want:
    bspc monitor HDMI-A-0 -d 1 2 3 4 5
    # Then, another:
    bspc monitor HDMI-A-1 -d 6 7 8 9 10
    # Whenever bspwm initializes a new monitor, it automatically
    # assigns it a desktop called Desktop.
    # We don't want it so let's remove that desktop Desktop:
    bspc desktop Desktop --remove > /dev/null
}

# This a function for when a monitor is disconnected
# or when there is no external monitor.
monitor_remove() {
    # First, we add a sort of temporary desktop to the external monitor.
    # You see, we can't just immediately move our desktops back to the
    # the first monitor because bspwm doesn't allow monitors without a
    # desktop. If a desktop is the only desktop on a monitor, you cannot
    # move it another.
    bspc monitor "$BSPWM_EXTERNALMONITOR" -a Desktop > /dev/null
    # Now that we have three desktops on the external monitor, we can
    # move the first desktop on it back to the internal monitor:
    bspc monitor HDMI-A-1 -d 1 2 3 4 5 6 7 8 9 10
    # Then, we can remove the monitor entirely:
    bspc monitor "$BSPWM_EXTERNALMONITOR" --remove > /dev/null
    # Lastly, we turn off the monitor:
    xrandr --output "$BSPWM_EXTERNALMONITOR" --off
}

# This is section is something similar to a main function
# in many programming languages.
# We just check if the external monitor is connected or not:
if xrandr | grep -o "$BSPWM_EXTERNALMONITOR connected" > /dev/null; then
    # If it is, we run the function above.
    # Notice here that we have to pass the parameters of
    # the script to the function. This is because a function's
    # parameter is different from the main script's parameter.
    # That's how shell scripting works but you already know that.
    monitor_add "$1" "$2"
else
    # If the external monitor is not connected,
    # we run the other function from above.
    # You might have noticed that I put a redirection to /dev/null
    # for some of the commands above. Those are the commands
    # that errors out when there isn't an external monitor to remove
    # (or to add) to begin with. That said, you don't have to worry
    # about them because they don't really affect any of the desktops
    # when that's the case (although someone more knowledgeable than me
    # on bspwm would probably disagree).
    monitor_remove "$1" "$2"
fi

# Here we (re-)set the background because newly added monitors to
# X usually have jacked up backgrounds unless you set a background
# to them.
#feh --no-fehbg --bg-scale path/to/some/image.jpg
# We check if the panel is running. If it is, we run the restart function
# above.
pgrep -x panel > /dev/null && reset_panel > /dev/null
