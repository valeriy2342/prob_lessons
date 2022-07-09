print('Медецинская анкета')
userName = input('Введите свое имя: ')
userFamili = input('Введите свою фамилию: ')
userOld = int(input('Введите свой возраст: '))
userWeight = int(input('Введите свой вес: '))
if userOld <= 30 and (userWeight > 50 and userWeight < 120):
print(userName, userFamili,',', userOld, 'лет',',', 'вес',userWeight ,'- хорошее состояние')
elif (userOld > 30 and userOld < 40) and (userWeight < 50 or userWeight > 120):
print(userName, userFamili,',', userOld, 'лет',',', 'вес',userWeight ,'- следует заняться собой')
elif userOld >= 40 and (userWeight < 50 or userWeight > 120):
print(userName, userFamili,',', userOld, 'лет',',', 'вес',userWeight ,'- следует обратиться к врачу')
else:
print(userName, userFamili,',', userOld, 'лет',',', 'вес',userWeight ,'- следует обратиться к врачу')