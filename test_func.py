file1 = {'key1': 'val1',
         'key2':{'key3':'val3'}}
file2 = {'key1': 'val2',
         'key2':{'key3':'val3'}}
keys = sorted(file1.keys() | file2.keys())
# print(file1.values())
# print(file2.values())
print(keys)