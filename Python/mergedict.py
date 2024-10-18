#merge dictionary
dict1 = {}
dict2 = {}

dict1 = {'a': 1, 'b': 2, 'c': 3 , 'common': 'CommonElement' }

dict2 = {'d': 4, 'e': 5, 'f': 6, 'common': 'CommonElement'}

merged_dict = {**dict1, **dict2}
merged_dict2 = dict1 | dict2
print(merged_dict)
print(merged_dict2)
