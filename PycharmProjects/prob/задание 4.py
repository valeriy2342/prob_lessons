my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for namber in (my_list_1)[:]:
    if namber in (my_list_2):
        my_list_1.remove(namber)
print(my_list_1)

