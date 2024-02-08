from aiohttp import web
import generator
import asyncio
import classes

routes = web.RouteTableDef()
templates = classes.FolderFiles ('templates')
templates.read_files ()

@routes.get ('/')
@routes.get ('/index.html')
async def main_page (request):
    text = ""
    for row in generator.mk_qft (data):
        text += f"<p> {row} </p>"
    html_page = templates.poem % ("2024", text)
    return web.Response (content_type = "text/html", text=html_page)

async def start_server ():
    app = web.Application()
    app.add_routes(routes)
    app.router.add_static('/static', path='static')
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()

async def main ():
    global data
    data = generator.load_data ("Без имени 1.csv")
    
    await start_server ()
    while 1:
        await asyncio.sleep (100)
 
asyncio.run (main ())
