import random

def spisok(input_list):
    if input_list:
        resultat = random.choice(input_list)
        return resultat

print(spisok([1, 2, 3, 4, 5, 6]))

print(spisok([]))