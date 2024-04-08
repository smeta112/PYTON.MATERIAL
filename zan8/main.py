
try:
    a = 10
    b = 0
    result = a/b
    print(result)
except ZeroDivisionError:
    print('Деление на ноль?')
except TypeError:
    print('A MISTAKE')
except FileNotFoundError:
    print('И откуда вы это взяли?')

finally:
    print('КОД РАБОТАЕТ НЕСМОТРЯ НА ОШИБКИ')


'''
try:
    #udhigasi
except ValueError:
    print("Ошибка: неверный ввод информации")
'''
'''
try:
    #udhigasi
except Имя_исключения:
    #code
'''