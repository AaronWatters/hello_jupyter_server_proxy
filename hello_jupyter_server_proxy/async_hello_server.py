
from aiohttp import web
#import asyncio

def script():
    import sys
    port = int(sys.argv[1])
    base_url = sys.argv[2]
    display_url = sys.argv[3]
    server = HelloServer(port, base_url, display_url)
    app = server.get_app()
    return web.run_app(app, port=port)

class HelloServer:

    def __init__(self, port, base_url, display_url):
        self.port = port
        self.base_url = base_url
        self.display_url = display_url

    async def hello(self, request):
        txt = """
        <h1>Hello world</h1>

        <p> Port is %s </p>
        <p> base_url is %s </p>
        <p> display_url is %s </p>
        """ % (self.port, self.base_url, self.display_url)
        b_body = txt.encode("utf-8")
        self.http_response = web.Response(body=b_body, content_type="text/html")
        return self.http_response

    def get_app(self):
        app = web.Application()
        app.router.add_route('GET', '/', self.hello)
        return app

if __name__ == "__main__":
    script()
