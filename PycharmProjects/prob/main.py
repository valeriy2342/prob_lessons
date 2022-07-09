name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
age = int(input('Введите ваш возраст: '))
the_weight = int(input('Введите ваш вес: '))

if age < 30:
print('')

if the_weight > 50 and the_weight < 120:
print(name, surname,',', age, 'лет,', 'вес',the_weight, '- Состояние хорошее')

elif age > 40:
print('')
if the_weight < 50 or the_weight > 120:
print(name, surname, ',', age, 'лет,', 'вес', the_weight, '- Требуется врачебный осмотр')

elif age > 30:
print('')
if the_weight < 50 or the_weight > 120:
print(name, surname, ',', age, 'лет,', 'вес', the_weight, '- Требуется занятся собой')

