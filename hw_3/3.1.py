s = input("Введите фразу: ")
print(f'Заглавных букв: {sum(map(str.isupper, s))}, строчных: {sum(map(str.islower, s))}')
