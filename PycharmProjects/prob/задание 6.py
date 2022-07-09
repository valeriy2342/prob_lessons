my_list_1 = [2, 2, 5, 12, 8, 2, 12]

resalt = []
for namber in my_list_1:
    if my_list_1.count(namber) == 1:
        resalt.append(namber)
print(resalt)