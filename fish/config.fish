source $HOME/.config/aliasrc

set fish_cursor_default block
set fish_cursor_insert line
set fish_cursor_replace_one underscore
set fish_visual block

# set fish_greeting ꦱ ꦩ꧀ꦱ ꦫ​ ꦑꦻ ꦫꦶ​ꦒ ꦫ ꦲ ꦂꦱ ꦪ 

# turn off vi mode indicator
function fish_mode_prompt 
end

# set vi mode as default 
set -g fish_key_bindings fish_vi_key_bindings

# keybindings
bind -M insert 'jj' 'set fish_bind_mode default ; commandline -f repaint'
bind -M insert \cf 'accept-autosuggestion'

set fish_color_selection --background='d79921'  
