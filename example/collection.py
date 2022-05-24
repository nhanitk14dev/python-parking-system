from cgi import print_arguments
from dataclasses import dataclass
from msilib import sequence
from typing import Tuple


# Mutable sequence: List

my_list = [1,2,3,4,5,6,7]
my_list_lang = ['Python', 'PHP', 'Java']
my_list_lang.append('Javascript')

# print(my_list_lang)
# print(my_list_lang[0])

# Immutable sequence: Tuple, String
# print(my_list[0:3])
# print(my_list[:-1])
# print(my_list[:-2])

# my_tupler = (1,2,3)
# mix_my_tupler = ('Python', 'PHP', True, [1, 3])
# print(my_tupler)

# my_set = {4,1,3}
# my_set.add(5)
# my_set.remove(1)
# print(my_set)


# Mapping - Dictionary
# my_dict = {'id': 1, 'name': 'Tom', 'gender': 'Famale'}
# my_dict['age'] = 26
# print(my_dict)
# print(my_dict.get('name'))
# print(my_dict['name'])
# key_id = 'id'
# print(key_id in my_dict.keys())
print(my_list[0] is 1)
