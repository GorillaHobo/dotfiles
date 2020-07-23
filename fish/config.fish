#alises

# Launch neovim
alias v="nvim"

# Neovim configuration
alias vfish="nvim ~/.config/fish/config.fish"
alias vbsp="nvim ~/.config/bspwm/bspwmrc"
alias vsx="nvim ~/.config/sxhkd/sxhkdrc"
alias vala="nvim ~/.config/alacritty/alacritty.yml"
alias vvim="nvim ~/.config/nvim/init.vim"

# nnn aliases 
alias n="nnn"
alias ndown="nnn ~/Storage/Downloads/"
alias nconf="nnn ~/.config/"
alias ns="nnn ~/Storage/"
alias nd="nnn ~/Documents/"
alias ndocs="nnn ~/Storage/Documents/"
alias yamaha="nnn ~/Storage/Documents/Yamaha/"
alias nex="nnn /run/media/tony/"
alias npoly="nnn ~/.config/polybar/"
alias nmtp="nnn ~/.mtp/"

# mount usb
alias usbmount="udisksctl mount -b /dev/sdc1"
alias usbunmount="udisksctl unmount -b /dev/sdc1"

# mount phone mtp
alias mtpmount="jmtpfs ~/.mtp"
alias mtpunmount="fusermount -u ~/.mtp"

# click on point to get RGB value
alias getrgb="maim -st 0 | convert - -resize 1x1\! -format '%[pixel:p{0,0}]' info:-"
