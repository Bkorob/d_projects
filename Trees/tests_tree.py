from hexlet import fs


# параметр mkdir создаёт директорию
# параметр mkfile создаёт файл
# вторыим параметром mkdir принимает список содержащий потомков

tree = fs.mkdir('etc', [
    fs.mkfile('bashrc', {'size': 100}),
    fs.mkdir('consul', [
        fs.mkfile('config.json'),
    ]),
],{'owner': 'nobody'})
print(tree)


{
'name': 'etc', 
'children': [
    {
    'name': 'bashrc', 
    'meta': {'size': 100}, 
    'type': 'file'
    }, 
    {
    'name': 'consul', 
    'children': [
    {
    'name': 'config.json', 
    'meta': {}, 
    'type': 'file'
    }
    ], 
    'meta': {}, 
    'type': 'directory'
    }
    ], 
    'meta': {'owner': 'nobody'}, 
    'type': 'directory'
    }