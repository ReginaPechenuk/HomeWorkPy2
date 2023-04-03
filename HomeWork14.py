#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import math
n = int(input('Введите натуральное число N ='))
i = 0
degree = round(math.sqrt(n),0)

result = 1
print('все целые степени двойки, не превосходящие числа N :')
while i <= degree:
    result = 2**i
    i+=1
    print(result)
