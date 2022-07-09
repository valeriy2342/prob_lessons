while True:
    namber = int(input(' Введите ваше число: '))
    if namber >0 and namber < 10:
        print(namber**2)
        break
    else: print('Число не верное ')
