import asyncio
import logging
from uuid import uuid4
from datetime import datetime

from sanic import Sanic
from datastar_py import ServerSentEventGenerator as SSE
from datastar_py.sanic import datastar_response


app = Sanic(__name__)
app.static('/static/', './static/')
app.static('/', './index.html', name="index")

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
        yield SSE.patch_elements(f"<span id='time'>{datetime.now().isoformat()}</span>")
        await asyncio.sleep(1)


if __name__ == "__main__":
    # while developing
    # app.run(debug=True, auto_reload=True, access_log=False)
    # else
    app.run(
    debug=False,
    auto_reload=True,
    unix="your_unix_sock_here"
    access_log=False)
