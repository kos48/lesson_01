"""Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк."""

user_second = int(input('enter time in seconds: '))

converted_hour = round(user_second / 3600)
converted_minutes = (round(user_second/60) % 60)
converted_seconds = user_second % 60

print(f'{converted_hour}:{converted_minutes}:{converted_seconds}')
