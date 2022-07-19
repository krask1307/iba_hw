# hw_2

1. Написать скрипт, если в файле есть слово "error", тогда удалить этот файл.
2. Написать скрипт, который будет создавать пользователя, имя пользователя должно вводится с клавиатуры.
Если пользователь существует, то вывести сообщение об этом.
3. Что такое systemd ?
---

1.
Create files:
```
touch file1 && echo eRRor > file2 && echo dvrvrtvrt > file3

-rwxr-xr-x 1 root root  409 Jul 12 16:49 12.sh*
-rw-r--r-- 1 root root    0 Jul 12 17:00 file1
-rw-r--r-- 1 root root    6 Jul 12 17:00 file2
-rw-r--r-- 1 root root   10 Jul 12 17:00 file3
-rw-r--r-- 1 root root   18 Jul 12 16:40 list
```

```shell
#!/bin/bash

/bin/ls -l |grep file |awk ' { print $9 } ' > ./list

# цикл по списку
file="./list"
IFS=$'\n'

# определяем переменную имени файла
for fname in $(cat $file)
do

err=$(cat ./$fname |grep -i "error" | tr [:upper:] [:lower:])

if [[ "$err" == "error" ]]

then
/bin/rm -rf ./$fname
echo "file $fname deleted"

else
echo "error not found"

fi

sleep 2

done
```

script output:
```
# ./12.sh
error not found
file file2 deleted
error not found
```

2.
```shell
#!/bin/bash

echo "enter name user"
read usr

cat /etc/passwd |grep $usr > /dev/null 2>&1
if [ $? -eq 0 ]
then
echo "user already exists"
else
useradd -m -N $usr && usermod -aG sudo $usr
echo "user created"
fi
```


3.
**systemd** - менеджер системы и служб, который выполняется как процесс с PID 1 и запускает остальную часть системы. systemd обеспечивает возможности агрессивной параллелизации, сокетную и D-Bus активацию для запуска служб, запуск демонов по запросу, отслеживание процессов с помощью контрольных групп Linux, обслуживание точек (авто)монтирования, а также предлагает развитую транзакционную логику управления службами на основе зависимостей. systemd поддерживает сценарии инициализации SysV и LSB и работает как замена sysvinit.
 
**systemd** поддерживает следующие типы модулей:

- .target — позволяет группировать модули, воплощая концепцию уровней запуска;
- .service — отвечает за запуск сервисов (служб), также поддерживает вызов интерпретаторов для исполнения пользовательских скриптов;
- .mount — отвечает за монтирование файловых систем;
- .automount — позволяет отложить монтирование файловых систем до фактического обращения к точке монтирования;
- .swap — отвечает за подключение файла или устройства подкачки;
- .timer — позволяет запускать модули по расписанию;
- .socket — предоставляет службам поддержку механизма сокет-активации;
- .slice — отвечает за создание контейнера cgroups;
- .device — позволяет реагировать на подключение устройств;
- .path — управляет иерархией файловой системы.
