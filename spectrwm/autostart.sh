#!/bin/bash
# xrandr -s 1920x1080
# sleep 1
# feh --bg-scale ~/.config/i3/Wallpapers/harrys.jpg &
feh --bg-scale ~/.config/leftwm/themes/basic_polybar/Dutch.jpg &
# parcellite for clipboard
parcellite -n &
# greenclip daemon
greenclip daemon &
# Starting polkit for auth dialogs
/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &
# Disable Caps Lock
setxkbmap -option caps:none &
