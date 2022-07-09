import random

number = random.randint(1, 100)
print(number)

while True:
    user_namber = int(input('Введите число: '))
    if user_namber==number:
        print('Вы угадали ')
        break
    elif user_namber > number:
        print('Введите число меньше')
    else:
            print('Введите число больше')

