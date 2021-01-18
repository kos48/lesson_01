"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции"""

user_number = input('Enter number: ')

i=0
max_number = 0

while i < len(user_number):
    if int(user_number[i]) > int(max_number):
        max_number = user_number[i]
    i+=1

print(max_number)
