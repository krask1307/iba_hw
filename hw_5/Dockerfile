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
