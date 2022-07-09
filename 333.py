

name = input('Введите имя: ')
age = int(input('Введите возраст: '))
citi = input('город: ')

def man(name, age, citi):
    return f'{name}, {age}года, проживает в городе {citi}'

print(man(name, age, citi))