call plug#begin()
Plug 'jiangmiao/auto-pairs'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-surround'
Plug 'itchyny/lightline.vim'
" Plug 'morhetz/gruvbox'
Plug 'easymotion/vim-easymotion'
" Plug 'omnisharp/omnisharp-vim'
Plug 'mhartington/oceanic-next'
Plug 'ap/vim-css-color'
Plug 'dag/vim-fish'
Plug 'shinchu/lightline-gruvbox.vim'
" Plug 'scrooloose/syntastic'
call plug#end()

" Or if you have Neovim >= 0.1.5
if (has("termguicolors"))
 set termguicolors
endif

" Theme
syntax enable
colorscheme default
" colorscheme OceanicNext

set number! relativenumber!
set autoindent
set tabstop=4 softtabstop=4
set shiftwidth=4
set smartindent

" set background=dark

let g:lightline = {}
let g:lightline.colorscheme = 'gruvbox'
let g:gruvbox_contrast = 'hard'

let mapleader=" "
" imap jj <Esc>
imap <C-f> <Esc>la
imap <C-b> <Esc>ha

" clear search box
nnoremap \ :noh<CR><CR>:<backspace>

nnoremap [<leader> o<Esc>k
nnoremap ]<leader> I<CR><Esc>

" save like doom emacs
nnoremap <leader>fs :w<CR>
nnoremap <leader>qq :q!<CR>

" Vim Easy Motion
nmap gsj <Plug>(easymotion-j)
nmap gsk <Plug>(easymotion-k)
nmap gss <Plug>(easymotion-s)
nmap cgss c<Plug>(easymotion-s)

