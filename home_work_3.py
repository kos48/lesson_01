"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn"""

user_number = input('enter number "n": ')
number_2 = int(user_number + user_number)
number_3 = int(user_number + user_number + user_number)

number = int(user_number) + number_2 + number_3
print('n+nn+nnn=', number)
