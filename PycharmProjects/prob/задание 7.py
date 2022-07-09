name =input('Введите ваше имя: ')
age =int(input('Введите ваш возраст: '))
city =input('Введите ваш город: ')

def seps(sep, text):
    print()
    print(sep*20 + text + sep*20)

def person_info(name, age, city):
    resultat = f'{name}, {age} год(а), проживает в городе {city}'
    return resultat


seps('*', ' Упражнение № 1 ')
print(person_info(name, age, city))