#SETURI

set_1 = {'mar', 'para', 'banana'}
set_2 = {1, 2, 3}

print(set_1, set_2)

set_1.remove('banana')  # daca elementul nu e in lista programul CRAPA
print(set_1)

set_1.discard('aprilie')  # programul NU CRAPA daca elementul nu e set
print(set_1)

set_1.pop()  # scoate ultimul element din set dar setul fiid neordonat nu avem control asupra acestui element
print(set_1)

# set_1.clear() - pt golirea setului

print(set_1.union(set_2))





