source $HOME/.config/aliasrc
export EDITOR=nvim
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
export PATH="$PATH:$HOME/.local/bin"
export PATH="$HOME/.config/emacs/bin:$PATH"

set fish_cursor_default block
set fish_cursor_insert line
set fish_cursor_replace_one underscore
set fish_visual block

# turn off vi mode indicator
function fish_mode_prompt 
end

# set vi mode as default 
set -g fish_key_bindings fish_vi_key_bindings

# keybindings
# bind -M insert 'jj' 'set fish_bind_mode default ; commandline -f repaint'
bind -M insert \cf 'accept-autosuggestion'
bind -M insert \ck 'up-or-search'
bind -M insert \cj 'down-or-search'

# get color from xresources
set fish_color_selection --background=(get_x_color 3) >/dev/null 2>&1
set fish_color_quote (get_x_color foreground) >/dev/null 2>&1
set fish_color_normal (get_x_color color8) >/dev/null 2>&1
set fish_color_comment (get_x_color color10) --bold >/dev/null 2>&1
set fish_color_command (get_x_color color12) --bold >/dev/null 2>&1
set fish_color_param (get_x_color color11) --bold >/dev/null 2>&1
set fish_color_autosuggestion (get_x_color color4)  >/dev/null 2>&1
set fish_color_redirection (get_x_color color10)  >/dev/null 2>&1
set fish_color_error (get_x_color color9)  >/dev/null 2>&1
