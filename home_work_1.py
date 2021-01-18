'''Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и
сохраните в переменные, выведите на экран.'''

"""создаём переменные разных типов"""
my_string = 'Hello, lession_01'
my_list =['lession_01', 'home_work', 56]
my_tuple = ('teacher', 'apprentice')
my_dictionary = {
    'name': 'Konstantin',
    'surname': 'Nikitin',
    'age':40,
    'city': 'Lipezk'
}
my_integer = 123
my_float = 12.3

"""выводим значения и их тип"""
print(my_string)
print(type(my_string))

print(my_list)
print(type(my_list))

print(my_tuple)
print(type(my_tuple))

print(my_dictionary)
print(type(my_dictionary))

print(my_integer)
print(type(my_integer))

print(my_float)
print(type(my_float))
"""запрашиваем у пользователя несколько строк и чисел, и выводим их значения и тип"""
user_number_int = int(input('insert the number: '))
print(user_number_int)
print(type(user_number_int))

user_number_float = float(input('insert the number: '))
print(user_number_float)
print(type(user_number_float))

user_name = input('what is your name?: ')
print(f'Hello, {user_name}')
print(type(user_name))

user_country_visits = [input('which countries have you visited?: ')]
print(user_country_visits)
print(type(user_country_visits))







