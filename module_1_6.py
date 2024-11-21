my_dict = {'Sasha':2000,'Vania':1999,'Dasha':2003,}
print(my_dict)
print(my_dict['Sasha'])
my_dict['Max'] = 2007
print(my_dict['Max'])
my_dict.update({'Lena':2002,'Gena':1995})
print(my_dict)
del my_dict['Sasha']
del my_dict['Dasha']
print(my_dict)


my_set = {1, 2, 3,True,'Int',3 , 2, 1,}
print(my_set)
my_set.add(4)
my_set.add(5)
my_set.remove(2)
print(my_set)