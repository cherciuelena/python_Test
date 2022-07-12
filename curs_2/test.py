my_list = [0, 1, 2, 3, 4]
text = "ana"
print(type(my_list))
print(my_list[2])
print(my_list[-1])
print(len(my_list))
print(len(text))

my_list.append('maria')
print(my_list)

print(my_list.index('maria'))  # introduce stringul 'maria' pe ultima pozitie

my_list.insert(3, 'trei')  # introduce stringul 'trei' pe pozitia 3 si deplaseaza restul listei cu un nr la dreapta
print(my_list)
print(my_list.index('maria')) # arata pe ce pozitie in lista se afla stringul 'maria'

"""Slicing"""

print(my_list[2:5])  # pt slicing ai nevoie de n+1  --> 2 'trei 3

print(my_list[2:])  # afiseaza toata lista de la indexul 2 la final

print(my_list[2:3:2]) # primil 2 repez de unde incepe - 3 reprez unde se sfarseste si ultimul 2 repez pasul

print(my_list[2::2])

print(my_list)
# print(my_list[7])
print(my_list[7:8])

print(my_list[len(my_list) - 1])

my_list.append(['A', 'B', 3, 'x', [4, 7,'w']])
print(my_list)

print(my_list[7][4][2])
print(my_list[7][2])

