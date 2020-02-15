" ================================================================
" Fisher's vimrc file.
" Author: Fisher
" Last change:  2020-02-01
" ================================================================

set nocompatible    " 关闭兼容模式, 默认情况下, Vim 会以兼容 Vi 的模式运行, 所以一定要关闭
set shortmess=atI   " 启动的时候不显示那个援助乌干达儿童的提示
filetype off        " 暂时关闭


" ================================================================
" vim-plug 插件
" ================================================================
call plug#begin('C:/VIM/vimfiles/plugins')
    Plug 'skywind3000/asyncrun.vim', { 'dir': '../vimfiles/plugins/vim-asyncrun'}
    Plug 'maralla/completor.vim', { 'dir': '../vimfiles/plugins/vim-completor'}
    Plug 'itchyny/lightline.vim', { 'dir': '../vimfiles/plugins/vim-lightline'}
    Plug 'ervandew/supertab', { 'dir': '../vimfiles/plugins/vim-supertab'}
    Plug 'yianwillis/vimcdoc', { 'dir': '../vimfiles/plugins/vim-doc'}
    Plug 'lyokha/vim-xkbswitch', { 'dir': '../vimfiles/plugins/vim-xkbswitch'}
    "Plug 'Yggdroot/indentLine',{'dir':'../vimfiles/plugins/vim-indentline'}
    Plug 'ctrlpvim/ctrlp.vim', { 'dir': '../vimfiles/plugins/vim-ctrlp'}
    Plug 'jiangmiao/auto-pairs', { 'dir': '../vimfiles/plugins/vim-auto-pairs'}
    Plug 'mg979/vim-visual-multi', { 'dir': '../vimfiles/plugins/vim-visual-multi'}
call plug#end()

" 自动检测文件类型和缩进格式, 并根据文件类型加载插件
filetype plugin indent on


" ================================================================
" Windows下引入gVim 原有配置
" ================================================================
if (has("win32") || has("win64"))
    " 模仿 Windows 快捷键, 例如 ctrl-s, ctrl-c, ctrl-v 等等
    source $VIMRUNTIME/mswin.vim
    " 模仿 Windows 的行为, 这一行很重要, 没有这行的话, 最大化经常出问题
    behave mswin
endif


" ================================================================
" UI和基本配置
" ================================================================
" 设置字体
if (has("win32") || has("win64"))
    "设置字体和大小
    set guifont=YaHei\ Consolas\ Hybrid:h12
    "设置初始窗口大小
    set lines=38 columns=186
    " 设定窗口位置
    winpos 132 86
endif
" GUI 的设置
if has("gui_running")
    " 显示菜单
    set guioptions+=m
    " 关闭工具栏
    set guioptions-=T
    " 关闭左侧滚动条
    set guioptions-=L
    " 关闭右侧滚动条
    set guioptions-=r
    " 设置Tab的样式为终端形式
    set guioptions-=e
    " 启动时最大化
    autocmd GUIEnter * simalt ~x
endif
" 只在需要的时候才重新绘制界面(例如宏执行过程中不需要重绘界面)
set lazyredraw
" 发生错误时不要响铃, 也不要闪烁
set noerrorbells
set belloff=all
" 分割窗口时保持相等的宽/高
set equalalways
" 竖直split时,在右边开启
set splitright
" 水平split时,在下边开启
set splitbelow
" 显示中文帮助
if version >= 603
    set helplang=cn
endif
"设置魔术"
set magic
set wildmenu " 增强版命令行，状态栏列出符合条件的命令
" 高亮匹配 <>
set mps+=<:>
" 共享剪贴板, 直接 yank or paste
set clipboard+=unnamed

" ================================================================
" 文件相关配置
"
" 关于备份文件的说明: 备份文件, 临时文件, undo 文件, 最好的做法是把
" 他们配置到单独的文件夹里, 我这里暂时都不让生成了, 以后可以按需要修改.
" 例如:
" set directory=~/.vim/.swp//
" set backupdir=~/.vim/.backup//
" set undodir=~/.vim/.undo//
" 注意最后要有两道//, 表示文件名使用绝对路径
" ================================================================
" 文件被外部改动后, 自动加载
set autoread
" 不生成备份文件
set nobackup
" 不生成临时文件
set noswapfile
" 不生成 undo 文件
set noundofile


" ================================================================
" 编辑器配置
" ================================================================
" 显示行号
set number
set showcmd         " 输入的命令显示出来，看的清楚些
" 显示语法高亮
syntax enable
syntax on
" 显示 tab(>---), 空格(^), 换行(¬)
set list
set listchars=tab:>-,trail:^ ",eol:¬
" 突出显示当前行
set cursorline
highlight CursorLine   cterm=NONE ctermbg=gray ctermfg=NONE guibg=NONE guifg=NONE
"用浅色高亮显示当前行"
autocmd InsertLeave * se nocul
autocmd InsertEnter * se cul
" 开启自动缩进
set autoindent
" 智能缩进
set smartindent
"设置行间距
set linespace=1
" 设置退格键能用
set backspace=indent,eol,start
" 编辑时按一个 Tab 键相当于输入4个空格
set tabstop=4
" 格式化时缩进尺寸为4个空格
set shiftwidth=4
" 让 Vim 把连续的空格视为一个 Tab, 删除时可以一次删掉一个 Tab 的空格数量
set softtabstop=4
" 把制表符转换为多个空格, 具体空格数量参考 tabstop 和 shiftwidth
set expandtab
" 在行和段的开始出使用 Tab
set smarttab
set scrolloff=3         " 光标移动到buffer的顶部和底部时保持3行距离
" 合并两行中文时, 不在中间加空格
set formatoptions+=B
" 合并行时不添加多余空格
set nojoinspaces
set ruler               " 在编辑过程中，在右下角显示光标位置的状态行
set laststatus=2        " 显示状态栏 (默认值为 1, 无法显示状态栏)
"通过使用: commands命令，告诉我们文件的哪一行被改变过"
set report=0
"带有如下符号的单词不要被换行分割"
set iskeyword+=_,$,@,%,#,-
" 设置魔术
set imcmdline

" ================================================================
" 主题
" ================================================================
colorscheme one
set background=light " dark or light
let g:lightline = {'colorscheme': 'one'}

" ================================================================
" 搜索和匹配
" ================================================================
" 高亮显示匹配的括号
set showmatch
" 高亮显示搜索到的关键字
set hlsearch
" 即时搜索
set incsearch
" 智能大小写敏感, 只要有一个字母大写, 就大小写敏感, 否则不敏感
set ignorecase smartcase
set foldmethod=indent   " 设置缩进折叠
set foldlevel=99        " 设置折叠层数
nnoremap <space> @=((foldclosed(line('.')) < 0) ? 'zc' : 'zo')<CR>
                        " 用空格键来开关折叠

" ================================================================
" 编码
" ================================================================
" 设置vim内部编码
set encoding=utf-8
" 设置编辑文件时的编码
set fileencoding=utf-8
" 设置 Vim 能识别的编码
set fileencodings=ucs-bom,utf-8,cp936,gb18030,gb2312,big5,cuc-jp,cuc-kr,latin
" 设置终端模式(非 GUI 模式)下的编码
set termencoding=utf-8
" 防止特殊符号无法显示
set ambiwidth=double
" 解决 Console 输出乱码
language messages zh_CN.utf-8
" 设置菜单编码
set langmenu=zh_CN.UTF-8
source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim

" ================================================================
" 一键运用Python
" ================================================================
map <F5> :call SaveRunPython()<CR>
func! SaveRunPython()
    exec "w"
    if &filetype == 'python'
        exec "AsyncRun -raw python %"
        exec "copen"
        exec "wincmd p"
    endif
endfunc
" 按照顺利输出控制台内容
let $PYTHONUNBUFFERED=1
" 解决Quickfix窗口乱码的问题
let g:asyncrun_encs = 'gbk'

" ================================================================
" 定义函数AutoSetFileHead，自动插入文件头
" ================================================================
autocmd BufNewFile *.py exec ":call AutoSetFileHead()"
function! AutoSetFileHead()
    "如果文件类型为python
    if &filetype == 'python'
        call setline(1, "\#!/usr/bin/env python")
        call append(1, "\# encoding: utf-8")
    endif

    normal G
    normal o
    normal o
endfunc

" ================================================================
" Remove trailing whitespace when writing a buffer, but not for diff files.
" ================================================================
function! RemoveTrailingWhitespace()
    if &ft != "diff"
        let b:curcol = col(".")
        let b:curline = line(".")
        silent! %s/\s\+$//
        silent! %s/\(\s*\n\)\+\%$//
        call cursor(b:curline, b:curcol)
    endif
endfunction
autocmd BufWritePre * call RemoveTrailingWhitespace()

" ================================================================
" 操作习惯和快捷键
" ================================================================
" 将 kk 配置成 esc
inoremap kk <esc>
" 按 U 执行 redo
noremap U <c-r>

" 对于很长的行, vim会自动换行, 此时 j 或者 k 就会一下跳很多行,
" 使用 gk,gj 可以避免跳过多行, 但是不方便, 所以做了如下映射.
nnoremap k gk
nnoremap j gj
vnoremap k gk
vnoremap j gj

" 将 <leader> 键配置为 ';'
let mapleader=';'


" ================================================================
" 插件相关配置
" ================================================================

" ----------------------------------------------------------------
" netrw
" ----------------------------------------------------------------
let g:netrw_browse_split = 4 "用前一个窗口打开文件
let g:netrw_liststyle = 3
let g:netrw_banner = 1
let g:netrw_winsize = 25

" ----------------------------------------------------------------
" SuperTab
" ----------------------------------------------------------------
"设置Tab键智能补全
let g:SuperTabDefaultCompletionType = "context"

" ----------------------------------------------------------------
" indentLine
" ----------------------------------------------------------------
"缩进指示线"
" let g:indentLine_char='┊'
" let g:indentLine_enabled = 1
let g:python_highlight_all = 1

"在 GUI 中快速改变字体大小
command! Bigger  :let &guifont = substitute(&guifont, '\d\+$', '\=submatch(0)+1', '')
command! Smaller :let &guifont = substitute(&guifont, '\d\+$', '\=submatch(0)-1', '')
