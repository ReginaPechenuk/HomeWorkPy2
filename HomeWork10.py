#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
#а некоторые – гербом. Определите минимальное число монеток, которые нужно 
#перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
n = int(input('Введите количество монеток на столе = '))
print('Статистическое распределение: 0 - это решки, 1 - это орлы')
i = 0
countReshki = 0
countOrel = 0
while i < n:
    money = randint(0,1)
    print(money)
    if money == 0:
        countReshki += 1
    elif money!=0:
        countOrel +=1
    i += 1
print()
print(f'Количество решек на столе = {countReshki}')
print(f'Количество орлов на столе = {countOrel}')
print()
if countReshki < countOrel:
    print(f'Минимальное количество для переворота монет это {countReshki} и это Решки')
elif countOrel<countReshki:
    print(f'Минимальное количество для переворота монет это {countOrel} и это Орлы')