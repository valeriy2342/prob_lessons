print('Медицинская анкета')
name = input('Введите ваше имя: ')
second_name = input('Введите вашу фамилию')
age= int(input('Введите ваш возраст: '))
ves= int(input('Введите ваш вес: '))
if age < 30 and ves > 50 and ves < 120:
    print('Пациент в хорошем состоянии')
elif age > 30 and age < 40 and (ves < 50 or ves > 120):
    print('Пациенту требуется заняться собой')
elif age > 40 and (ves < 50 or ves > 120):
    print('Пациенту требуется врачебный осмотр')