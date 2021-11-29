# Пользователь вводит целые числа. Должна произойти ошибка, если введенное число нечетное.
while True:
    try:
        num = int(input('Enter an integer: '))
        if num % 2 == 1: raise ValueError('The number must be even')
        else: break
    except ValueError as ve:
        print(ve)


num = int(input('Enter an integer: '))
if num % 2 == 1: raise ValueError('The number must be even')
else: print()