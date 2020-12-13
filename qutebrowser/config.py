import subprocess
import os

# ============================
# Color Settings
# ============================

def read_xresources(prefix):
    """
    read settings from xresources
    """
    props = {}
    x = subprocess.run(["xrdb", "-query"], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split("\n")
    for line in filter(lambda l: l.startswith(prefix), lines):
        prop, _, value = line.partition(":\t")
        props[prop] = value
    return props

xresources = read_xresources("*")

# ============================
# Color Scheme
# ============================

# black           = '#282828'
# white           = '#ebdbb2'
# blue            = '#458588'
# lightblue       = '#83a598'
# yellow          = '#d79921'
# lightyellow     = '#fabd2f'
# red             = '#cc241d'
# lightred        = '#fb4934'
# green           = '#689d6a'
# lightgreen      = '#b8bb26'
# magenta         = '#b16286'
# lightmagenta    = '#d3869b'

black           = xresources["*.color0"]
white           = xresources["*.color15"]
blue            = xresources["*.color4"]
lightblue       = xresources["*.color12"]
yellow          = xresources["*.color3"]
lightyellow     = xresources["*.color11"]
red             = xresources["*.color1"]
lightred        = xresources["*.color9"]
green           = xresources["*.color6"]
lightgreen      = xresources["*.color10"]
magenta         = xresources["*.color5"]
lightmagenta    = xresources["*.color13"]
lightwhite      = xresources["*.color7"]
background      = xresources["*.background"]
foreground      = xresources["*.foreground"]

c.colors.completion.category.bg = blue
c.colors.completion.category.border.bottom = blue
c.colors.completion.category.border.top = blue
c.colors.completion.category.fg = white
c.colors.completion.even.bg =  black
c.colors.completion.fg = [white, yellow, white]
c.colors.completion.item.selected.bg = yellow
c.colors.completion.item.selected.border.bottom = yellow
c.colors.completion.item.selected.border.top = yellow
c.colors.completion.item.selected.fg = black
c.colors.completion.item.selected.match.fg = white
c.colors.completion.match.fg = yellow
c.colors.completion.odd.bg = black
c.colors.completion.scrollbar.bg = black
c.colors.completion.scrollbar.bg = '#333333'#
c.colors.completion.scrollbar.fg = white
# c.colors.contextmenu.disabled.bg = None
# c.colors.contextmenu.disabled.fg = None
# c.colors.contextmenu.menu.bg = None
# c.colors.contextmenu.menu.fg = None
# c.colors.contextmenu.selected.bg = None
# c.colors.contextmenu.selected.fg = None
c.colors.downloads.bar.bg = black
c.colors.downloads.error.bg = red
c.colors.downloads.error.fg = white
c.colors.downloads.start.bg = yellow
c.colors.downloads.start.fg = black
c.colors.downloads.stop.bg = blue
c.colors.downloads.stop.fg = white
c.colors.downloads.system.bg = 'none'
c.colors.downloads.system.fg = 'none'
c.colors.hints.bg = lightyellow
c.colors.hints.fg = black
c.colors.hints.match.fg = white
c.colors.keyhint.bg = 'rgba(40, 40, 40, 90%)'
c.colors.keyhint.fg = white
c.colors.keyhint.suffix.fg = yellow
c.colors.messages.error.bg = red
c.colors.messages.error.border = red
c.colors.messages.error.fg = white
c.colors.messages.info.bg = black
c.colors.messages.info.border = black
c.colors.messages.info.fg = white
c.colors.messages.warning.bg = yellow
c.colors.messages.warning.border = yellow
c.colors.messages.warning.fg = white
c.colors.prompts.bg = black
c.colors.prompts.border = '0px solid black'   
c.colors.prompts.fg = white
c.colors.prompts.selected.bg = yellow
c.colors.statusbar.caret.bg = magenta
c.colors.statusbar.caret.fg = white
c.colors.statusbar.caret.selection.bg = lightmagenta
c.colors.statusbar.caret.selection.fg = white
c.colors.statusbar.command.bg = black
c.colors.statusbar.command.fg = white
c.colors.statusbar.command.private.bg = black
c.colors.statusbar.command.private.fg = white
c.colors.statusbar.insert.bg = blue
c.colors.statusbar.insert.fg = white
c.colors.statusbar.normal.bg = black
c.colors.statusbar.normal.fg = white
c.colors.statusbar.passthrough.bg = green
c.colors.statusbar.passthrough.fg = white
c.colors.statusbar.private.bg = black
c.colors.statusbar.private.fg = yellow
c.colors.statusbar.progress.bg = white
c.colors.statusbar.url.error.fg = red
c.colors.statusbar.url.fg = white
c.colors.statusbar.url.hover.fg = green
c.colors.statusbar.url.success.http.fg = lightgreen
c.colors.statusbar.url.success.https.fg = blue
c.colors.statusbar.url.warn.fg = yellow
c.colors.tabs.bar.bg = blue
c.colors.tabs.even.bg = black
c.colors.tabs.even.fg = white
c.colors.tabs.indicator.error = red
c.colors.tabs.indicator.start = blue
c.colors.tabs.indicator.stop = blue
# c.colors.tabs.indicator.system = 'rgb'
c.colors.tabs.odd.bg = black
c.colors.tabs.odd.fg = white
c.colors.tabs.pinned.even.bg = black
c.colors.tabs.pinned.even.fg = white
c.colors.tabs.pinned.odd.bg = black
c.colors.tabs.pinned.odd.fg = white
c.colors.tabs.pinned.selected.even.bg = blue
c.colors.tabs.pinned.selected.even.fg = white
c.colors.tabs.pinned.selected.odd.bg = blue
c.colors.tabs.pinned.selected.odd.fg = white
c.colors.tabs.selected.even.bg = lightblue
c.colors.tabs.selected.even.fg = lightwhite
c.colors.tabs.selected.odd.bg = lightblue
c.colors.tabs.selected.odd.fg = lightwhite
# c.colors.webpage.bg = white
# c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
# c.colors.webpage.darkmode.contrast = 0.0

# c.colors.webpage.darkmode.enabled = False

# c.colors.webpage.darkmode.grayscale.all = False

# c.colors.webpage.darkmode.grayscale.images = 0.0

# c.colors.webpage.darkmode.policy.images = 'never'

# c.colors.webpage.darkmode.policy.page = 'smart'

# c.colors.webpage.darkmode.threshold.background = 0

# c.colors.webpage.darkmode.threshold.text = 256

# c.colors.webpage.prefers_color_scheme_dark = False

# ============================
# General Settings
# ============================

# c.completion.cmd_history_max_items = 100

# c.completion.delay = 0

# c.completion.height = '50%'

c.completion.open_categories = ['quickmarks', 'bookmarks', 'history']

# c.completion.quick = True

# c.completion.scrollbar.padding = 2

# c.completion.scrollbar.width = 12

# c.completion.show = 'always'

c.completion.shrink = True

# c.completion.timestamp_format = '%Y-%m-%d'

# c.completion.use_best_match = False

# c.completion.web_history.exclude = []

# c.completion.web_history.max_items = -1

c.confirm_quit = ['downloads']

# c.content.autoplay = True

# c.content.cache.appcache = True

# c.content.cache.maximum_pages = 0

# c.content.cache.size = None

# c.content.canvas_reading = True

# c.content.cookies.accept = 'all'

# c.content.cookies.store = True

# c.content.default_encoding = 'iso-8859-1'

# c.content.desktop_capture = 'ask'

# c.content.dns_prefetch = True

# c.content.frame_flattening = False

# c.content.fullscreen.overlay_timeout = 3000

# c.content.fullscreen.window = False

# c.content.geolocation = 'ask'

# c.content.headers.accept_language = 'en-US,en;q=0.9'

# c.content.headers.custom = {}

# c.content.headers.do_not_track = True

# c.content.headers.referer = 'same-domain'

# c.content.headers.user_agent = 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}'

# c.content.host_blocking.enabled = True

# c.content.host_blocking.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']

# c.content.host_blocking.whitelist = []

# c.content.hyperlink_auditing = False

# c.content.images = True

# c.content.javascript.alert = True

# c.content.javascript.can_access_clipboard = False

# c.content.javascript.can_close_tabs = False

# c.content.javascript.can_open_tabs_automatically = False

# c.content.javascript.enabled = True

# c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}

# c.content.javascript.modal_dialog = False

# c.content.javascript.prompt = True

# c.content.local_content_can_access_file_urls = True

# c.content.local_content_can_access_remote_urls = False

# c.content.local_storage = True

# c.content.media_capture = 'ask'

# c.content.mouse_lock = 'ask'

# c.content.mute = False

# c.content.netrc_file = None

# c.content.notifications = 'ask'

# c.content.pdfjs = False

# c.content.persistent_storage = 'ask'

# c.content.plugins = False

# c.content.print_element_backgrounds = True

# c.content.private_browsing = False

# c.content.proxy = 'system'

# c.content.proxy_dns_requests = True

# c.content.register_protocol_handler = 'ask'

# c.content.site_specific_quirks = True

# c.content.ssl_strict = 'ask'

# c.content.unknown_url_scheme_policy = 'allow-from-user-interaction'

# c.content.user_stylesheets = []

# c.content.webgl = True

# c.content.webrtc_ip_handling_policy = 'all-interfaces'

# c.content.xss_auditing = False

c.downloads.location.directory = '/home/tony/Storage/Downloads/'

# c.downloads.location.prompt = True

# c.downloads.location.remember = True

# c.downloads.location.suggestion = 'path'

# c.downloads.open_dispatcher = None

c.downloads.position = 'bottom'

# c.downloads.remove_finished = -1

# c.editor.command = ['nvim', '{file}' ]
# c.editor.command = ['nvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']

# ============================
# Fonts Settings
# ============================

# c.fonts.completion.category = 'bold default_size default_family'

# c.fonts.completion.entry = 'default_size default_family'

# c.fonts.contextmenu = 'default-size default-family'

# c.fonts.debug_console = 'default_size default_family'

# c.fonts.default_family = []

c.fonts.default_size = '9pt'

# c.fonts.downloads = 'default_size default_family'

c.fonts.hints = 'bold 13px default_family'

# c.fonts.keyhint = 'default_size default_family'

# c.fonts.messages.info = 'default_size default_family'

# c.fonts.messages.warning = 'default_size default_family'

# c.fonts.prompts = 'default_size sans-serif'

# c.fonts.statusbar = 'default_size default_family'

# c.fonts.tabs.selected = 'default_size default_family'

# c.fonts.tabs.unselected = 'default_size default_family'

# c.fonts.web.family.cursive = ''

# c.fonts.web.family.fantasy = ''

# c.fonts.web.family.fixed = ''

# c.fonts.web.family.sans_serif = 'Noto Sans'

# c.fonts.web.family.serif = ''

c.fonts.web.family.standard = 'SNFS Display'

c.fonts.web.size.default = 15

c.fonts.web.size.default_fixed = 14

# c.fonts.web.size.minimum = 0

# c.fonts.web.size.minimum_logical = 6

# ============================
# Browser Settings
# ============================

# c.hints.auto_follow = 'unique-match'

# c.hints.auto_follow_timeout = 0

c.hints.border = '0px solid #E3BE23'

c.hints.chars = 'asdfghjkl'

# c.hints.dictionary = '/usr/share/dict/words'

# c.hints.find_implementation = 'python'

# c.hints.hide_unmatched_rapid_hints = True

# c.hints.leave_on_load = True

# c.hints.min_chars = 1

# c.hints.mode = 'letter'

# c.hints.next_regexes = ['\\bnext\\b', '\\bmore\\b', '\\bnewer\\b', '\\b[>→≫]\\b', '\\b(>>|»)\\b', '\\bcontinue\\b']

# c.hints.padding = {'top': 0, 'bottom': 0, 'left': 3, 'right': 3}

# c.hints.prev_regexes = ['\\bprev(ious)?\\b', '\\bback\\b', '\\bolder\\b', '\\b[<←≪]\\b', '\\b(<<|«)\\b']

c.hints.radius = 0

# c.hints.scatter = True

# c.hints.selectors = {'all': ['a', 'area', 'textarea', 'select', 'input:not([type="hidden"])', 'button', 'frame', 'iframe', 'img', 'link', 'summary', '[onclick]', '[onmousedown]', '[role="link"]', '[role="option"]', '[role="button"]', '[ng-click]', '[ngClick]', '[data-ng-click]', '[x-ng-click]', '[tabindex]'], 'links': ['a[href]', 'area[href]', 'link[href]', '[role="link"][href]'], 'images': ['img'], 'media': ['audio', 'img', 'video'], 'url': ['[src]', '[href]'], 'inputs': ['input[type="text"]', 'input[type="date"]', 'input[type="datetime-local"]', 'input[type="email"]', 'input[type="month"]', 'input[type="number"]', 'input[type="password"]', 'input[type="search"]', 'input[type="tel"]', 'input[type="time"]', 'input[type="url"]', 'input[type="week"]', 'input:not([type])', 'textarea']}

# c.hints.uppercase = False

# c.history_gap_interval = 30

# c.input.escape_quits_reporter = True

# c.input.forward_unbound_keys = 'auto'

# c.input.insert_mode.auto_enter = True

# c.input.insert_mode.auto_leave = True

# c.input.insert_mode.auto_load = False

# c.input.insert_mode.leave_on_load = True

# c.input.insert_mode.plugins = False

# c.input.links_included_in_focus_chain = True

# c.input.mouse.back_forward_buttons = True

# c.input.mouse.rocker_gestures = False

# c.input.partial_timeout = 5000

# c.input.spatial_navigation = False

# c.keyhint.blacklist = []

c.keyhint.delay = 100

c.keyhint.radius = 0

# c.logging.level.console = 'info'

# c.logging.level.ram = 'debug'

c.messages.timeout = 3000

# c.new_instance_open_target = 'tab'

# c.new_instance_open_target_window = 'last-focused'

# c.prompt.filebrowser = True

c.prompt.radius = 0

# c.qt.args = []

# c.qt.force_platform = None

# c.qt.force_platformtheme = None

# c.qt.force_software_rendering = 'none'

# c.qt.highdpi = False

# c.qt.low_end_device_mode = 'auto'

# c.qt.process_model = 'process-per-site-instance'

# c.scrolling.bar = 'overlay'

# c.scrolling.smooth = True

# c.search.ignore_case = 'smart'

# c.search.incremental = True

# c.search.wrap = True

# c.session.default_name = None

# c.session.lazy_restore = False

# c.spellcheck.languages = []

# c.statusbar.padding = {'top': 1, 'bottom': 1, 'left': 0, 'right': 0}

# c.statusbar.position = 'bottom'

c.statusbar.show = 'always'

# c.statusbar.widgets = ['keypress', 'url', 'scroll', 'history', 'tabs', 'progress']

# c.tabs.background = False

# c.tabs.close_mouse_button = 'middle'

# c.tabs.close_mouse_button_on_bar = 'new-tab'

# c.tabs.favicons.scale = 1.0

# c.tabs.favicons.show = 'always'

# c.tabs.focus_stack_size = 10

# c.tabs.indicator.padding = {'top': 2, 'bottom': 2, 'left': 0, 'right': 4}

# c.tabs.indicator.width = 3

# c.tabs.last_close = 'ignore'

# c.tabs.max_width = -1

# c.tabs.min_width = -1

# c.tabs.mode_on_change = 'normal'

# c.tabs.mousewheel_switching = True

# c.tabs.new_position.related = 'next'

# c.tabs.new_position.stacking = True

# c.tabs.new_position.unrelated = 'last'

# c.tabs.padding = {'top': 0, 'bottom': 0, 'left': 5, 'right': 5}

# c.tabs.pinned.frozen = True

# c.tabs.pinned.shrink = True

# c.tabs.position = 'top'

# c.tabs.select_on_remove = 'next'

c.tabs.show = 'always'

c.tabs.show_switching_delay = 5000

# c.tabs.tabs_are_windows = False

# c.tabs.title.alignment = 'left'

c.tabs.title.format = '{audio}{index}: {current_title} {private}'

# c.tabs.title.format_pinned = '{index}'

# c.tabs.tooltips = True

# c.tabs.undo_stack_size = 100

# c.tabs.width = '20%'

# c.tabs.wrap = True

# ============================
# Search Settings
# ============================

# c.url.auto_search = 'naive'

# c.url.default_page = 'https://start.duckduckgo.com/'

# c.url.incdec_segments = ['path', 'query']

# c.url.open_base_url = False

c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    'd': 'https://duckduckgo.com/?q={}',
    'g' : 'https://www.google.com/search?q={}',
    'y' : 'https://yandex.com/search/?msid=1600227532.21776.97936.549811&text={}&suggest_reqid=189617456160022753274905091117279',
    'b' : 'https://www.bing.com/search?q={}',
    'id' : 'https://duckduckgo.com/?q={}&iax=images&ia=images',
    'ig' : 'https://www.google.com/search?q={}&tbm=isch&ved=2ahUKEwjuhfWY3-zrAhUlJHIKHYLiCLAQ2-cCegQIABAA&oq=texx&gs_lcp=CgNpbWcQAzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzoCCAA6BQgAELEDUO0nWOEvYMg2aABwAHgAgAGHC4gByRSSAQM3LTKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=2IdhX-65NqXIyAOCxaOACw&safe=strict',
    'ib' : 'https://www.bing.com/images/search?q={}&form=HDRSC2&first=1&scenario=ImageBasicHover',
    'iy' : 'https://yandex.com/images/search?text={}&from=tabbar',
    'yt' : 'https://www.youtube.com/results?search_query={}',
    }
# c.url.searchengines = {'g' : 'https://www.google.com/search?q={}'}

c.url.start_pages = ['https://start.duckduckgo.com']

# c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']

# c.window.hide_decoration = False

# c.window.title_format = '{perc}{current_title}{title_sep}qutebrowser'

# c.zoom.default = '100%'

# c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']

# c.zoom.mouse_divider = 512

# c.zoom.text_only = False

# ============================
# Key Bindings
# ============================

# config.bind('$', 'move-to-end-of-line', mode='caret')
# config.bind('0', 'move-to-start-of-line', mode='caret')
# config.bind('<Ctrl-Space>', 'drop-selection', mode='caret')
# config.bind('<Escape>', 'leave-mode', mode='caret')
# config.bind('<Return>', 'yank selection', mode='caret')
# config.bind('<Space>', 'toggle-selection', mode='caret')
# config.bind('G', 'move-to-end-of-document', mode='caret')
# config.bind('H', 'scroll left', mode='caret')
# config.bind('J', 'scroll down', mode='caret')
# config.bind('K', 'scroll up', mode='caret')
# config.bind('L', 'scroll right', mode='caret')
# config.bind('[', 'move-to-start-of-prev-block', mode='caret')
# config.bind(']', 'move-to-start-of-next-block', mode='caret')
# config.bind('b', 'move-to-prev-word', mode='caret')
# config.bind('c', 'enter-mode normal', mode='caret')
# config.bind('e', 'move-to-end-of-word', mode='caret')
# config.bind('gg', 'move-to-start-of-document', mode='caret')
# config.bind('h', 'move-to-prev-char', mode='caret')
# config.bind('j', 'move-to-next-line', mode='caret')
# config.bind('k', 'move-to-prev-line', mode='caret')
# config.bind('l', 'move-to-next-char', mode='caret')
# config.bind('o', 'reverse-selection', mode='caret')
# config.bind('v', 'toggle-selection', mode='caret')
# config.bind('w', 'move-to-next-word', mode='caret')
# config.bind('y', 'yank selection', mode='caret')
# config.bind('{', 'move-to-end-of-prev-block', mode='caret')
# config.bind('}', 'move-to-end-of-next-block', mode='caret')

config.bind('<Ctrl-k>', 'completion-item-focus prev', mode='command')
config.bind('<Ctrl-j>', 'completion-item-focus next', mode='command')
config.bind('<Ctrl-h>', 'completion-item-focus --history prev', mode='command')
config.bind('<Ctrl-l>', 'completion-item-focus --history next', mode='command')
# config.bind('<Alt-B>', 'rl-backward-word', mode='command')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='command')
# config.bind('<Alt-D>', 'rl-kill-word', mode='command')
# config.bind('<Alt-F>', 'rl-forward-word', mode='command')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='command')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='command')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='command')
# config.bind('<Ctrl-C>', 'completion-item-yank', mode='command')
# config.bind('<Ctrl-D>', 'completion-item-del', mode='command')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='command')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='command')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='command')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='command')
# config.bind('<Ctrl-N>', 'command-history-next', mode='command')
# config.bind('<Ctrl-P>', 'command-history-prev', mode='command')
# config.bind('<Ctrl-Return>', 'command-accept --rapid', mode='command')
# config.bind('<Ctrl-Shift-C>', 'completion-item-yank --sel', mode='command')
# config.bind('<Ctrl-Shift-Tab>', 'completion-item-focus prev-category', mode='command')
# config.bind('<Ctrl-Tab>', 'completion-item-focus next-category', mode='command')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='command')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='command')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='command')
# config.bind('<Down>', 'completion-item-focus --history next', mode='command')
# config.bind('<Escape>', 'leave-mode', mode='command')
# config.bind('<Return>', 'command-accept', mode='command')
# config.bind('<Shift-Delete>', 'completion-item-del', mode='command')
# config.bind('<Shift-Tab>', 'completion-item-focus prev', mode='command')
# config.bind('<Tab>', 'completion-item-focus next', mode='command')
# config.bind('<Up>', 'completion-item-focus --history prev', mode='command')

# config.bind('<Ctrl-B>', 'hint all tab-bg', mode='hint')
# config.bind('<Ctrl-F>', 'hint links', mode='hint')
# config.bind('<Ctrl-R>', 'hint --rapid links tab-bg', mode='hint')
# config.bind('<Escape>', 'leave-mode', mode='hint')
# config.bind('<Return>', 'follow-hint', mode='hint')

# config.bind('<Ctrl-E>', 'open-editor', mode='insert')
# config.bind('<Escape>', 'leave-mode', mode='insert')
# config.bind('<Shift-Ins>', 'insert-text -- {primary}', mode='insert')

# config.bind('<Shift-Escape>', 'leave-mode', mode='passthrough')

# config.bind('<Alt-B>', 'rl-backward-word', mode='prompt')
# config.bind('<Alt-Backspace>', 'rl-backward-kill-word', mode='prompt')
# config.bind('<Alt-D>', 'rl-kill-word', mode='prompt')
# config.bind('<Alt-F>', 'rl-forward-word', mode='prompt')
# config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='prompt')
# config.bind('<Alt-Y>', 'prompt-yank', mode='prompt')
# config.bind('<Ctrl-?>', 'rl-delete-char', mode='prompt')
# config.bind('<Ctrl-A>', 'rl-beginning-of-line', mode='prompt')
# config.bind('<Ctrl-B>', 'rl-backward-char', mode='prompt')
# config.bind('<Ctrl-E>', 'rl-end-of-line', mode='prompt')
# config.bind('<Ctrl-F>', 'rl-forward-char', mode='prompt')
# config.bind('<Ctrl-H>', 'rl-backward-delete-char', mode='prompt')
# config.bind('<Ctrl-K>', 'rl-kill-line', mode='prompt')
# config.bind('<Ctrl-P>', 'prompt-open-download --pdfjs', mode='prompt')
# config.bind('<Ctrl-U>', 'rl-unix-line-discard', mode='prompt')
# config.bind('<Ctrl-W>', 'rl-unix-word-rubout', mode='prompt')
# config.bind('<Ctrl-X>', 'prompt-open-download', mode='prompt')
# config.bind('<Ctrl-Y>', 'rl-yank', mode='prompt')
# config.bind('<Down>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Escape>', 'leave-mode', mode='prompt')
# config.bind('<Return>', 'prompt-accept', mode='prompt')
# config.bind('<Shift-Tab>', 'prompt-item-focus prev', mode='prompt')
# config.bind('<Tab>', 'prompt-item-focus next', mode='prompt')
# config.bind('<Up>', 'prompt-item-focus prev', mode='prompt')

# config.bind('<Escape>', 'leave-mode', mode='register')

# config.bind('<Alt-Shift-Y>', 'prompt-yank --sel', mode='yesno')
# config.bind('<Alt-Y>', 'prompt-yank', mode='yesno')
# config.bind('<Escape>', 'leave-mode', mode='yesno')
# config.bind('<Return>', 'prompt-accept', mode='yesno')
# config.bind('N', 'prompt-accept --save no', mode='yesno')
# config.bind('Y', 'prompt-accept --save yes', mode='yesno')
# config.bind('n', 'prompt-accept no', mode='yesno')
# config.bind('y', 'prompt-accept yes', mode='yesno')

config.bind(';V', 'spawn mpv {url}')
config.bind(';v', 'hint links spawn mpv {hint-url}')
config.bind('ed', 'hint links spawn st -e aria2c --dir=/home/tony/Storage/Downloads \'{hint-url}\'')
config.bind('et', 'hint links spawn st -e aria2c --dir=/home/tony/Storage/Downloads/Torrents --seed-time=0 \'{hint-url}\'')
# config.bind('ev', 'hint links spawn st -e youtube-dl --config-location ~/.config/youtube-dl/config \'{hint-url}\'')
config.bind('ev', 'hint links userscript youtube_video_downloader')
config.bind('ea', 'hint links userscript youtube_audio_downloader')
# config.bind('ea', 'hint links spawn st -e youtube-dl --config-location ~/.config/youtube-dl/music \'{hint-url}\'')

config.bind(';z', 'hint images download')
config.bind('<Ctrl-Shift-h>', 'tab-move -')
config.bind('<Ctrl-Shift-l>', 'tab-move +')
config.bind('j', 'scroll-px 0 75')
config.bind('k', 'scroll-px 0 -75')
config.bind('h', 'scroll-px -75 0')
config.bind('l', 'scroll-px 75 0')
config.bind('<Ctrl-R>', ':config-source')
config.bind('<Ctrl-U>', 'undo')
config.unbind('D')
config.bind('<Ctrl-Shift-q>', 'tab-close -o')
config.bind('<Ctrl-j>', 'back')
config.bind('<Ctrl-h>', 'tab-prev')
config.bind('<Ctrl-k>', 'forward')
config.bind('u', 'scroll-page 0 -0.5')
config.bind('d', 'scroll-page 0 0.5')
config.bind('<Ctrl-q>', 'tab-close')
config.bind('<Ctrl-l>', 'tab-next')
config.bind('<Ctrl-Shift-O>', 'set-cmd-text -s :open -b')
# config.bind("'", 'enter-mode jump_mark')
# config.bind('+', 'zoom-in')
# config.bind('-', 'zoom-out')
# config.bind('.', 'repeat-command')
# config.bind('/', 'set-cmd-text /')
# config.bind(':', 'set-cmd-text :')
# config.bind(';I', 'hint images tab')
# config.bind(';O', 'hint links fill :open -t -r {hint-url}')
# config.bind(';R', 'hint --rapid links window')
# config.bind(';Y', 'hint links yank-primary')
# config.bind(';b', 'hint all tab-bg')
# config.bind(';d', 'hint links download')
# config.bind(';f', 'hint all tab-fg')
# config.bind(';h', 'hint all hover')
# config.bind(';i', 'hint images')
# config.bind(';o', 'hint links fill :open {hint-url}')
# config.bind(';r', 'hint --rapid links tab-bg')
# config.bind(';t', 'hint inputs')
# config.bind(';y', 'hint links yank')
# config.bind('<Alt-1>', 'tab-focus 1')
# config.bind('<Alt-2>', 'tab-focus 2')
# config.bind('<Alt-3>', 'tab-focus 3')
# config.bind('<Alt-4>', 'tab-focus 4')
# config.bind('<Alt-5>', 'tab-focus 5')
# config.bind('<Alt-6>', 'tab-focus 6')
# config.bind('<Alt-7>', 'tab-focus 7')
# config.bind('<Alt-8>', 'tab-focus 8')
# config.bind('<Alt-9>', 'tab-focus -1')
# config.bind('<Alt-m>', 'tab-mute')
# config.bind('<Ctrl-A>', 'navigate increment')
# config.bind('<Ctrl-Alt-p>', 'print')
# config.bind('<Ctrl-B>', 'scroll-page 0 -1')
# config.bind('<Ctrl-D>', 'scroll-page 0 0.5')
# config.bind('<Ctrl-F5>', 'reload -f')
# config.bind('<Ctrl-F>', 'scroll-page 0 1')
# config.bind('<Ctrl-N>', 'open -w')
# config.bind('<Ctrl-PgDown>', 'tab-next')
# config.bind('<Ctrl-PgUp>', 'tab-prev')
# config.bind('<Ctrl-Q>', 'quit')
# config.bind('<Ctrl-Return>', 'follow-selected -t')
# config.bind('<Ctrl-Shift-N>', 'open -p')
# config.bind('<Ctrl-Shift-T>', 'undo')
# config.bind('<Ctrl-Shift-Tab>', 'nop')
# config.bind('<Ctrl-Shift-W>', 'close')
# config.bind('<Ctrl-T>', 'open -t')
# config.bind('<Ctrl-Tab>', 'tab-focus last')
# config.bind('<Ctrl-U>', 'scroll-page 0 -0.5')
# config.bind('<Ctrl-V>', 'enter-mode passthrough')
# config.bind('<Ctrl-W>', 'tab-close')
# config.bind('<Ctrl-X>', 'navigate decrement')
# config.bind('<Ctrl-^>', 'tab-focus last')
# config.bind('<Ctrl-h>', 'home')
# config.bind('<Ctrl-p>', 'tab-pin')
# config.bind('<Ctrl-s>', 'stop')
# config.bind('<Escape>', 'clear-keychain ;; search ;; fullscreen --leave')
# config.bind('<F11>', 'fullscreen')
# config.bind('<F5>', 'reload')
# config.bind('<Return>', 'follow-selected')
# config.bind('<back>', 'back')
# config.bind('<forward>', 'forward')
# config.bind('=', 'zoom')
# config.bind('?', 'set-cmd-text ?')
# config.bind('@', 'run-macro')
# config.bind('B', 'set-cmd-text -s :quickmark-load -t')
# config.bind('D', 'tab-close -o')
# config.bind('F', 'hint all tab')
# config.bind('G', 'scroll-to-perc')
# config.bind('H', 'back')
# config.bind('J', 'tab-next')
# config.bind('K', 'tab-prev')
# config.bind('L', 'forward')
# config.bind('M', 'bookmark-add')
# config.bind('N', 'search-prev')
# config.bind('O', 'set-cmd-text -s :open -t')
# config.bind('PP', 'open -t -- {primary}')
# config.bind('Pp', 'open -t -- {clipboard}')
# config.bind('R', 'reload -f')
# config.bind('Sb', 'open qute://bookmarks#bookmarks')
# config.bind('Sh', 'open qute://history')
# config.bind('Sq', 'open qute://bookmarks')
# config.bind('Ss', 'open qute://settings')
# config.bind('T', 'tab-focus')
# config.bind('V', 'enter-mode caret ;; toggle-selection --line')
# config.bind('ZQ', 'quit')
# config.bind('ZZ', 'quit --save')
# config.bind('[[', 'navigate prev')
# config.bind(']]', 'navigate next')
# config.bind('`', 'enter-mode set_mark')
# config.bind('ad', 'download-cancel')
# config.bind('b', 'set-cmd-text -s :quickmark-load')
# config.bind('cd', 'download-clear')
# config.bind('co', 'tab-only')
# config.bind('d', 'tab-close')
# config.bind('<Ctrl-q>', 'tab-close')
# config.bind('f', 'hint')
# config.bind('g$', 'tab-focus -1')
# config.bind('g0', 'tab-focus 1')
# config.bind('gB', 'set-cmd-text -s :bookmark-load -t')
# config.bind('gC', 'tab-clone')
# config.bind('gD', 'tab-give')
# config.bind('gO', 'set-cmd-text :open -t -r {url:pretty}')
# config.bind('gU', 'navigate up -t')
# config.bind('g^', 'tab-focus 1')
# config.bind('ga', 'open -t')
# config.bind('gb', 'set-cmd-text -s :bookmark-load')
# config.bind('gd', 'download')
# config.bind('gf', 'view-source')
# config.bind('gg', 'scroll-to-perc 0')
# config.bind('gi', 'hint inputs --first')
# config.bind('gl', 'tab-move -')
# config.bind('gm', 'tab-move')
# config.bind('go', 'set-cmd-text :open {url:pretty}')
# config.bind('gr', 'tab-move +')
# config.bind('gt', 'set-cmd-text -s :buffer')
# config.bind('gu', 'navigate up')
# config.bind('h', 'scroll left')
# config.bind('i', 'enter-mode insert')
# config.bind('j', 'scroll down')
# config.bind('k', 'scroll up')
# config.bind('l', 'scroll right')
# config.bind('m', 'quickmark-save')
# config.bind('n', 'search-next')
# config.bind('o', 'set-cmd-text -s :open')
# config.bind('pP', 'open -- {primary}')
# config.bind('pp', 'open -- {clipboard}')
# config.bind('q', 'record-macro')
# config.bind('r', 'reload')
# config.bind('sf', 'save')
# config.bind('sk', 'set-cmd-text -s :bind')
# config.bind('sl', 'set-cmd-text -s :set -t')
# config.bind('ss', 'set-cmd-text -s :set')
# config.bind('tCH', 'config-cycle -p -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('tCh', 'config-cycle -p -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('tCu', 'config-cycle -p -u {url} content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('tIH', 'config-cycle -p -u *://*.{url:host}/* content.images ;; reload')
# config.bind('tIh', 'config-cycle -p -u *://{url:host}/* content.images ;; reload')
# config.bind('tIu', 'config-cycle -p -u {url} content.images ;; reload')
# config.bind('tPH', 'config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload')
# config.bind('tPh', 'config-cycle -p -u *://{url:host}/* content.plugins ;; reload')
# config.bind('tPu', 'config-cycle -p -u {url} content.plugins ;; reload')
# config.bind('tSH', 'config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tSh', 'config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tSu', 'config-cycle -p -u {url} content.javascript.enabled ;; reload')
# config.bind('tcH', 'config-cycle -p -t -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('tch', 'config-cycle -p -t -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('tcu', 'config-cycle -p -t -u {url} content.cookies.accept all no-3rdparty never ;; reload')
# config.bind('th', 'back -t')
# config.bind('tiH', 'config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload')
# config.bind('tih', 'config-cycle -p -t -u *://{url:host}/* content.images ;; reload')
# config.bind('tiu', 'config-cycle -p -t -u {url} content.images ;; reload')
# config.bind('tl', 'forward -t')
# config.bind('tpH', 'config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload')
# config.bind('tph', 'config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload')
# config.bind('tpu', 'config-cycle -p -t -u {url} content.plugins ;; reload')
# config.bind('tsH', 'config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tsh', 'config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload')
# config.bind('tsu', 'config-cycle -p -t -u {url} content.javascript.enabled ;; reload')
# config.bind('u', 'undo')
# config.bind('v', 'enter-mode caret')
# config.bind('wB', 'set-cmd-text -s :bookmark-load -w')
# config.bind('wIh', 'devtools left')
# config.bind('wIj', 'devtools bottom')
# config.bind('wIk', 'devtools top')
# config.bind('wIl', 'devtools right')
# config.bind('wIw', 'devtools window')
# config.bind('wO', 'set-cmd-text :open -w {url:pretty}')
# config.bind('wP', 'open -w -- {primary}')
# config.bind('wb', 'set-cmd-text -s :quickmark-load -w')
# config.bind('wf', 'hint all window')
# config.bind('wh', 'back -w')
# config.bind('wi', 'devtools')
# config.bind('wl', 'forward -w')
# config.bind('wo', 'set-cmd-text -s :open -w')
# config.bind('wp', 'open -w -- {clipboard}')
# config.bind('xO', 'set-cmd-text :open -b -r {url:pretty}')
# config.bind('xo', 'set-cmd-text -s :open -b')
# config.bind(';o', 'hint links fill :open {hint-url}')
# config.bind('yD', 'yank domain -s')
# config.bind('yM', 'yank inline [{title}]({url}) -s')
# config.bind('yP', 'yank pretty-url -s')
# config.bind('yT', 'yank title -s')
# config.bind('yY', 'yank -s')
# config.bind('yd', 'yank domain')
# config.bind('ym', 'yank inline [{title}]({url})')
# config.bind('yp', 'yank pretty-url')
# config.bind('yt', 'yank title')
# config.bind('yy', 'yank')
# config.bind('{{', 'navigate prev -t')
# config.bind('}}', 'navigate next -t')

config.bind(',ap', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/apprentice/apprentice-all-sites.css ""')

config.bind(',dr', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/darculized/darculized-all-sites.css ""')

config.bind(',gr', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css ""')

config.bind(',sd', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css ""')

config.bind(',sl', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css ""')

config.bind("<Ctrl-h>", "fake-key <BackSpace>", "insert")
config.bind("<Ctrl-a>", "fake-key <Home>", "insert")
config.bind("<Ctrl-e>", "fake-key <End>", "insert")
config.bind("<Ctrl-b>", "fake-key <Left>", "insert")
config.bind("<Mod1-b>", "fake-key <Ctrl-Left>", "insert")
config.bind("<Ctrl-f>", "fake-key <Right>", "insert")
config.bind("<Mod1-f>", "fake-key <Ctrl-Right>", "insert")
config.bind("<Ctrl-k>", "fake-key <Up>", "insert")
config.bind("<Ctrl-j>", "fake-key <Down>", "insert")
config.bind("<Mod1-d>", "fake-key <Ctrl-Delete>", "insert")
config.bind("<Ctrl-d>", "fake-key <Delete>", "insert")
config.bind("<Ctrl-w>", "fake-key <Ctrl-Backspace>", "insert")
config.bind("<Ctrl-u>", "fake-key <Shift-Home><Delete>", "insert")
config.bind("<Ctrl-l>", "fake-key <Shift-End><Delete>", "insert")
