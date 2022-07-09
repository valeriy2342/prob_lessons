
def attack(person1, person2):
    person2['health'] = person2['health'] - person1['damage']
    print(f'Игрок "{person1["name"]}" [{person1["health"]}] нанёс {person1["damage"]} урона игроку "{defender["name"]}" [{defender["health"]}]')

player1 = input('Введите имя игрока 1: ')
player2 = input('Введите имя игрока 2: ')
player = {'name': player1, 'health': 80, 'damage': 40}
enemy = {'name': player2, 'health': 70, 'damage': 30}

attack(player, enemy)