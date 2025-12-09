import asyncio
import logging
from uuid import uuid4
from datetime import datetime

from sanic import Sanic
from datastar_py import ServerSentEventGenerator as SSE
from datastar_py.sanic import datastar_response

from nitro.infrastructure.html import Span
from base import *

app = Sanic(__name__)
app.static('/static/', './static/')

@app.get("/")
@app_template(title="Nitro Datastart")
def index(request):
    return Div(
        H1("Nitro Datastart your App", cls="text-4xl font-bold mb-4"),    
        Span("Loading...", id="time"),    
        cls="px-8 lg:px-16 xl:px-32 mt-16",
        data_init="@get('/load')"
    )


logging.basicConfig(filename='perso.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_response
async def cookie(request, response):
    if not request.cookies.get("user_id"):
        user_id = uuid4().hex
        response.add_cookie('user_id', user_id)

@app.get("/load")
@datastar_response
async def load(request):
    while True:
        yield SSE.patch_elements(Span(datetime.now().isoformat(), id="time"))
        await asyncio.sleep(1)


if __name__ == "__main__":
    # while developing
    app.run(debug=True, auto_reload=True, access_log=False)
    # else
    # app.run(
    # debug=False,
    # auto_reload=True,
    # unix="your_unix_sock_here",
    # access_log=False)
