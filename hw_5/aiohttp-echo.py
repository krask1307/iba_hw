#! /usr/bin/python3
from aiohttp import web
from datetime import datetime
import json


async def say_hello(request):
    return web.Response(text='Hello, {}\n'.format(request.match_info['name']))


async def post_handler(request):
    data = await request.json()
    username, password = data['username'], data['password']
    print(datetime.now(), 'POST request:\n', json.dumps(data, indent=4))
    return web.json_response(data)

app = web.Application()
app.add_routes([web.get('/{name}', say_hello)])
app.add_routes([web.post('/', post_handler)])

web.run_app(app, port=8080)
