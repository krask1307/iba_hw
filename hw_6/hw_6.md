# hw_6
1. Через volume подкинуть конфиг в nginx контейнер, чтобы на страничке в браузере появилась надпись Docker (либо через curl это проверить). 
---



**1.**
```sh
# tree ./
./
├── docker-compose.yml
├── hosts
│   └── docker.conf
├── logs
│   └── nginx
│       ├── access.log
│       └── error.log
└── www
    └── index.html
```


<br>

docker-compose.yml
```yaml
version: '3'

services:
  nginx:
    image: nginx:latest
    restart: always
    container_name: nginx_hw6
    volumes:
       - ./hosts:/etc/nginx/conf.d
       - ./www:/var/www
       - ./logs/nginx:/var/log/nginx
    ports:
      - "8080:80"
    networks:
      back:
        ipv4_address: 172.16.238.2
      default:

networks:
  back:
    driver: bridge
    attachable: true
    ipam:
     driver: default
     config:
       - subnet: 172.16.238.0/24
  default:
    driver: bridge
```
<br>

Nginx docker.conf
```nginx
server {
    listen       80;

    location / {
        root   /var/www;
        index  index.html index.htm;
    }
}
```
<br>

index.html
```html
Docker hw_6
```
<br>

Run docker-compose:
```
# docker-compose up -d
```
<br>


CURL output:
```
# curl http://localhost:8080
Docker hw_6

---

curl http://172.16.238.2:80
Docker hw_6
```

<br>

![Alt text](https://github.com/krask1307/iba_hw/blob/master/hw_6/screenshots/hw_6.png)
