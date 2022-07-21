# hw_5
1. Зарегистрироваться в Dockerhub.
2. Создать свой любой имадж(использовать Dockerfile) и запушить в свой репозиторий в Dockerhub.
---



**1.**
```
# docker login
Username: krask1307
Password:

Login Succeeded
```


<br>
<br>

**2.**

Dockerfile
```Dockerfile
FROM alpine:3.10

# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
ENV PYTHONUNBUFFERED=1

# python3
RUN apk add --no-cache python3 && \
  if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
  python3 -m ensurepip && \
  rm -r /usr/lib/python*/ensurepip && \
  pip3 install --no-cache --upgrade pip setuptools wheel && \
  if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

WORKDIR /www
COPY requirements.txt ./
RUN apk --update add --no-cache --virtual build-dependencies gcc python3-dev musl-dev && \
  pip install --requirement requirements.txt && \
  apk del build-dependencies

COPY aiohttp-echo.py ./
ENTRYPOINT [ "python", "aiohttp-echo.py" ]

```
<br>

aiohttp-echo.py
```python
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
```
<br>

requirements.txt
```
astroid==2.1.0
certifi==2018.11.29
chardet==3.0.4
gunicorn==19.9.0
httpie==1.0.2
httpie-jwt-auth==0.3.0
idna==2.8
isort==4.3.4
lazy-object-proxy==1.3.1
Markdown==3.0.1
mccabe==0.6.1
PyJWT==1.7.1
requests==2.21.0
six==1.12.0
urllib3==1.24.1
wrapt==1.11.1
```
<br>

Run build image:
```
# docker build -t krask1307/hw_docker:v1 .
```
<br>



<br>

Push image to Dockerhub:
```
# docker push krask1307/hw_docker:v1

The push refers to repository [docker.io/krask1307/hw_docker]
3d10962c44a7: Pushed
cee19722d7fd: Pushed
61e996dd395e: Pushed
58c149a8d8e4: Pushed
cb72e68dc285: Pushed
9fb3aa2f8b80: Mounted from library/alpine
v1: digest: sha256:d1a6117d08dcc35f2790c5606bcdad7bca3d814d555d6f5921ad2bf8f4855fe5 size: 1571
```

Link: https://hub.docker.com/repository/docker/krask1307/hw_docker
