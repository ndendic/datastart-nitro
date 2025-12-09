from nitro.infrastructure.html import *
from nitro.infrastructure.html.components import *

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
                onclick="document.dispatchEvent(new CustomEvent('basecoat:sidebar'))",
                cls="mr-auto"
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
                cls='scrollbar'
            ),
            aria_label='Sidebar navigation'
        ),
        data_side='left',
        aria_hidden='false',
        cls='sidebar'
    )

