# hw_3
1. Написать скрипт, пользователь вводит строку из букв в нижнем регистре и верхнем регистре. Нужно посчитать, сколько в этой строке больших букв.
2. Написать скрипт, который будет делать ping google.com. Если сервер отвечает, то выводить - success, если нет - doesn't work.
3. Написать скрипт, который будет выводить текущую дату и время.
---



1.
```python
# cat 3.1.py
s = input("Введите фразу: ")
print(f'Заглавных букв: {sum(map(str.isupper, s))}, строчных: {sum(map(str.islower, s))}')
```
```
# python3 3.1.py
Введите фразу: JHBJHmfk kjnrJJJJ
Заглавных букв: 9, строчных: 7
```


2.
```python
# cat 3.2.py

import os

def check_ping():
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname + "> /dev/null")

    if response == 0:
        pingstatus = "SUCCESS"
    else:
        pingstatus = "DOESN'T WORK"

    return pingstatus

pingstatus = check_ping()

print(pingstatus)
```
```diff
# python3 3.2.py
+ SUCCESS
```

3.
```python
# cat 3.3.py
import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y %H:%M"))
```
```
# python3 3.3.py
19-07-2022 13:19
```
