#!/bin/bash
bspc subscribe monitor_add monitor_geometry | while read -r line; do
            if [ "$(bspc query -M | wc -l)" -eq "2" ]; then
                bspc monitor ^1 -d 1 2 3 4 5
                bspc monitor ^2 -d 6 7 8 9 0
            else
                bspc monitor -d 1 2 3 4 5 6 7 8 9 0
            fi
done &
