n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
n3 = int(input('Введите третье число: '))

def numbers(n1, n2, n3):
    return max(n1, n2, n3)

print(numbers(n1, n2, n3))


name =input('Введите имя: ')
age = int(input('Введите возраст: '))
citi = input('город: ')

def man (name, age, citi):
    return f' {name), {age}, проживает в городе {citi}"'

printman (name, age, citi)