my_list = [4, 7, 9, 'ana', 0, 11, 'mere']

print(my_list.index(9))  # trebuie pus elementul intre paranteze ca sa iti arate pozitia pe care se afla in lista aka indexul

my_list.append(6)
print(my_list)

my_list.insert(2, 'george')
print(my_list)

print(len(my_list))

my_list.remove(6)
print(my_list)

my_list.pop(0)  # 0 reprezita elementul de pe indexul 0 nu cifra 0 din lista -  scoate elementul de pe indexul 0 din lista
print(my_list)

ultimul_element = my_list.pop()  # scoate ultimul element din lista - nu il stocheaza undeva
print(my_list)
print(ultimul_element)  # am atribuit unei variabile ultimul element prin functia pop() si atunci s-a stocat

# my_list.clear()
# print(my_list)

another_list = my_list.copy()
print(another_list)

another_another_list = list(my_list)
print(another_another_list)

my_list.reverse()
print(my_list)

my_list.append('ana')
print(my_list.count('ana'))

final_list = another_list + another_another_list
print(final_list)

my_list.extend(another_list)
print(my_list)
