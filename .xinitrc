# alsactl restore -f $HOME/.config/alsa/asound.store
xrdb $HOME/.config/XResources

# switch capslock with escape key
setxkbmap -option caps:swapescape
xinput set-prop 12 321 1

#set brightness to default (50
# sudo light -I

feh --bg-fill $HOME/.local/share/bg

slstatus &
picom &
sxhkd &
launch_dunst &

#start emacs daemon
emacs --bg-daemon 
doom-change-theme

syncthing --no-browser &

# exec dwm
while :; do
	ssh-agent dwm
done
