# DICTIONARE

my_dictionary = {
    'key_1': 12,
    'key_2': 4 + 5j,
    3: True,
    4: None,
    5 + 2j: 'a',
    ('key_6', 7): [1, 2, 3],
    -8: ('First', 'Second', 'Third')
}

# Accesare valoare dictionar
print(my_dictionary['key_1'])

# Accesare valoare dictionar folosind metdoda .get()
print(my_dictionary.get('key_1'))
print(my_dictionary.get('key_7'))

print(my_dictionary.get('key_1', 'My custom value'))
print(my_dictionary.get('key_7', 'My custom value'))

print(my_dictionary[3])
# print(my_dictionary[6])  # aici crapa programul
print(my_dictionary.get(6))
print(my_dictionary)  # valoarea introdusa prin .get() nu se pastreaza permanent in dictionarul initial pt asta trebuie folosita functia .update()

print(len(my_dictionary))
# pt a adauga intr-un dictionar se fol .update
my_dictionary.update({'key_update': 'update'})
print(my_dictionary)

# Goleste dic
# my_dictionary.clear()
# print(my_dictionary)

# copy dic
print(my_dictionary.copy())

# keys - returneaza toate chiele dintr-un dictionar ->> returneaza dict_keys
print(my_dictionary.keys())

# values - returneaza toate valorile dintr-un dictionar ->> returneaza dict_values
print(my_dictionary.values())

# items - returneaza toate elementele dintr-un dictionar - un element reprezita un tuplu de forma (cheie: valoare)
print(my_dictionary.items())
      
# pop(key) - scoate cheia din dictionar
my_dictionary.pop(4)
print(my_dictionary)

# popitem() - scoate din dictionar ultimul element
my_dictionary.popitem()
print(my_dictionary)


# iterarea prin dictionare 
dictionar = {'1': 'val1', '2': 'val2', '3': 'val3'}

    # atat dictionar cat si dictionar.keys() vor apela DOAR cheile dintr-un dictionar 
for i in dictionar:
    print(i)
    
for i in dictionar.keys():
    print(i)

for i in dictionar.items():
    # print(i, '=>>')
    index, value = i
    print('i:', i, 'index:', index, 'value =>>', value)

print(my_dictionary)

for i in my_dictionary.items():
    # print(i, '=>>')
    index, value = i
    print('i:', i, 'index:', index, 'value =>>', value)
    
for i in dictionar:
    print(i, '=>>', dictionar[i])
print(dictionar)

for i in my_dictionary:
    print(i, '=>>', my_dictionary[i])
print(my_dictionary)

