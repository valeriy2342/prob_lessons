import random

number = random.randint(1, 100)
# print(number)

user_namber = None
count = 0
lavels ={1 : 10, 2 : 5, 3 : 3}
lavel = int(input('Выберете уровень сложности: '))
max_count = lavels[lavel]

user_count = int(input('Введите количество играков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя игрока {i+1} :')
    users.append(user_name)

print(users)


while number != user_namber:
    count += 1
    if count > max_count:
        print('Все игроки проиграли! ')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход игрока {user}')
        
    user_namber = int(input('Введите число: '))

    if user_namber > number:
        print('Введите число меньше')
    elif user_namber < number:
            print('Введите число больше')
    else:
        print('Вы угадали ')