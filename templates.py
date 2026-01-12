from sanic.response import html
from nitro import *  # noqa: F403
from nitro.html import *  # noqa: F403
from nitro.html.components import *  # noqa: F403
from nitro.html import template as templ
from components import Sidebar, Navbar

# Shared page template
htmlkws = dict(lang="en", data_resize="true")
page = page_template(htmlkw=htmlkws, lucide=True)


@templ
def template(content, title: str):
    return page(
        Fragment(
            Sidebar(),
            Main(
                Navbar(),
                Div(
                    Div(content, id="content"),
                    cls="p-4 md:p-6 xl:p-12",
                ),
            ),
        ),
        title=title,
        wrap_in=html,
    )
