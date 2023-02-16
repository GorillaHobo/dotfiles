source $HOME/.config/aliasrc
export EDITOR=nvim
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
export PATH="$PATH:$HOME/.local/bin"
export PATH="$PATH:$HOME/.config/emacs/bin"
export PATH="$PATH:$HOME/.config/composer/vendor/bin"
export GOPATH="$HOME/Documents/go"
export NVM_DIR="$HOME/.config/nvm"
export ANDROID_HOME="/opt/android-sdk"
export MsBuildSDKsPath="/usr/share/dotnet/sdk/6.*/Sdks"
# set PATH $PATH:$ANDROID_HOME/cmdline-tools/latest/bin
# set PATH $PATH:$ANDROID_HOME/tools/bin export 
# set PATH $PATH:$ANDROID_HOME/platform-tools

set -gx NVM_DIR $HOME/.config/nvm
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
# set fish_color_selection --background=(get_x_color 3)
set fish_color_normal white --bold
set fish_color_command bryellow --bold
set fish_color_redirection magenta --bold
set fish_color_error red --bold
set fish_color_param normal --bold
set fish_color_comment white --bold
set fish_color_quote normal --bold
set fish_color_search_match cyan --bold
set fish_color_autosuggestion blue --bold
set fish_color_cancel brred --bold

set fish_pager_color_progress brcyan --bold
set fish_pager_color_prefix yellow --bold
set fish_pager_color_completion brblue --bold
set fish_pager_color_description magenta
set fish_pager_color_selected_background --background=brblue
set fish_pager_color_selected_prefix black
set fish_pager_color_selected_completion black
set fish_pager_color_selected_description black

