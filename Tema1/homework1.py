# 1.Declarare lista
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_list_asc = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_list_desc = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# 2.Ordonare ascendenta lista
my_list_asc.sort()
print(my_list_asc)

# 3.Ordonare descendenta lista
my_list_desc.sort(reverse=True)
print(my_list_desc)

# 4.Even numbers
print(my_list_asc[1::2])

# 5.Odd numbers
print(my_list_asc[::2])

# 6.Multiplii de 3
print(my_list_asc[2::3])