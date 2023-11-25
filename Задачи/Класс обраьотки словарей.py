import copy


# BEGIN (write your solution here)
class InMemoryKV():
    def __init__(self, dict_):
        self.dict_ = copy.deepcopy(dict_)

    def set_(self, key, value):
        self.dict_.update({key: value})

    def unset_(self, key):
        self.dict_.pop(key)

    def get_(self, key, default=None):
        return self.dict_.get(key, default)

    def to_dict(self):
        return copy.deepcopy(self.dict_)
    

# data = {'key': 10}
# data_copy = copy.deepcopy(data)
# map = InMemoryKV(data)
    
# data['key2'] = 'value2'
# print(map.to_dict())
    
# map2 = map.to_dict()
# map2['key2'] = 'value2'
# print(map.to_dict()) # == data_copy


def swap_key_value(item):
    new_dict = item.to_dict()
    
    for k in new_dict:
        item.unset_(k)
    for k, v in new_dict.items():
        item.set_(v, k)
    
        
        
    
    
# map = InMemoryKV({'foo': 'bar', 'bar': 'zoo'})
# swap_key_value(map)


# {'bar': 'foo', 'zoo': 'bar'} == {'foo': 'bar', 'bar': 'foo'}

map = InMemoryKV({'key': 10})
map.set_('key2', 'value2')
swap_key_value(map)
assert map.get_('key') is None
assert map.get_(10) == 'key'
assert map.get_('value2') == 'key2'
print(map.to_dict())