# alsactl restore -f $HOME/.config/alsa/asound.store
xrdb $HOME/.config/XResources

#start emacs daemon
emacs --daemon &

# switch capslock with escape key
setxkbmap -option caps:swapescape

#set brightness to default (50
sudo light -I


feh --bg-fill $HOME/.local/share/bg

slstatus &
picom &
sxhkd &
launch_dunst &

syncthing --no-browser &

# exec dwm
while :; do
	ssh-agent dwm
done
