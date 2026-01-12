from nitro.html import *
from nitro.html.components import *

THEMES = [
    ('Claude', 'claude'),
    ('Candy', 'candy'),
    ('Neo Brutalism', 'neo-brutal'),
    ('Dark Matter', 'darkmatter'),
]

def ThemeSelector():
    return Select(
        Optgroup(
            *[Option(theme[0], value=theme[1]) for theme in THEMES],
        ),
        bind='theme',
        on_change="document.documentElement.setAttribute('data-theme', $theme);",
        cls='select w-[180px]'
    )

def ThemeSwitcher():
    return Button(
        LucideIcon('sun'),
        on_click="$darkMode = !$darkMode; $darkMode ? document.documentElement.classList.add('dark') : document.documentElement.classList.remove('dark');", 
        cls="btn"
    )

def Navbar():
    return Header(
        Div(
            Button(
                LucideIcon('panel-left'), 
                type='button', 
                on_click="$sidebar_open = !$sidebar_open",
                cls="mr-auto",
                variant="ghost",
            ),
            Div(
                ThemeSelector(),
                ThemeSwitcher(),
                cls="flex gap-2"
            ),
            cls='flex h-14 w-full items-center gap-2 px-4'
        ),
        cls='bg-background sticky inset-x-0 top-0 isolate flex shrink-0 items-center gap-2 border-b z-10'
    )

def Sidebar():
    return Aside(
        Nav(
            Header(
                A(
                    Div(
                        LucideIcon('zap', cls="h-4 w-4"),                        
                        cls='bg-sidebar-primary text-sidebar-primary-foreground flex aspect-square size-8 items-center justify-center rounded-lg'
                    ),
                    Div(
                        Span('My', Span('Boosted', cls='truncate font-light'),cls='truncate font-bold'),
                        Span('Application', cls='truncate text-xs font-light'),
                        cls='grid flex-1 text-left text-sm leading-tight'
                    ),
                    href='/',
                    aria_current='page',
                    cls='btn-ghost p-2 h-12 w-full justify-start'
                )
            ),
            Section(
                Div(
                    H3('Getting started', id='group-label-content-1'),
                    Ul(
                        Li(A(LucideIcon('home'),Span('Home'),href='#')),
                        Li(
                            Details(
                                Summary(
                                    LucideIcon('settings-2'),
                                    'Settings',
                                    aria_controls='submenu-content-1-3-content'
                                ),
                                Ul(
                                    Li(A(Span('General'),href='#')),
                                    Li(A(Span('Team'),href='#')),
                                    Li(A(Span('Billing'),href='#')),
                                    Li(A(Span('Limits'),href='#')),
                                    id='submenu-content-1-3-content'
                                ),
                                id='submenu-content-1-3'
                            )
                        )
                    ),
                    role='group',
                    aria_labelledby='group-label-content-1'
                ),
                cls='scrollbar',            
            ),

            aria_label='Sidebar navigation',
            on_click__outside="if ($resize_is_mobile && $sidebar_open && !evt.target.closest('[data-sidebar-toggle]')) {$sidebar_open = false;}",
        ),
        data_side='left',
        aria_hidden='false',
        data_sidebar_initialized='true',
        **{'data-attr:aria-hidden': '!$sidebar_open'},
        signals=Signals(sidebar_open=True),
        cls='sidebar',        
    )