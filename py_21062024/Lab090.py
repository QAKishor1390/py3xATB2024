# my_dict = {'b': 2, 't': 6, 'V': 10, 'F': 30}
# print(my_dict)
#key > value

my_dict = dict()
my_dict['z'] = 44
my_dict['c'] = 89
my_dict['k'] = 498
my_dict['p'] = 47
my_dict['x'] = 98

print(my_dict)

for k,v in my_dict.items():
    print(k,v)
    print(len(my_dict))
    print(type(k))
    print(type(v))