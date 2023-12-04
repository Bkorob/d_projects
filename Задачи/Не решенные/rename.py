<<<<<<< HEAD
class People:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name
    

class Hello:
    def prints(self, people, nn):
        greers = people(nn)
        print(f'hello, {greers.get_name()}!')


a = Hello()
a.prints(People, '11')
=======
def sum_(number):
    return sum(int(x) ** 2 for x in str(number))


# BEGIN (write your solution here)
def is_happy_number(num):
    a = sum_(num)
    for x in range(10):
        a = sum_(a)
    return int(a) == 10


print(is_happy_number(1))

# from requests import get


# import json
# import yaml

# def parse_file(path, ):
#     filepath = path.split('.')
#     if filepath[-1] in ['yaml', 'yml']:
#         with open(path) as p_y:
#             source = yaml.safe_load(p_y)
#             return source
#     elif filepath[-1] == 'json':
#         with open(path) as p_j:
#             source = json.load(p_j)
#             return source
#     raise ValueError('Unsupported file format')

# json_data =   get("https://something.com/json-data").text
# parsed_data = parse_file(json_data, 'json')
>>>>>>> ff8864247b20f62348317199eda91ef4d9947a01
