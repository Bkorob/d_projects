# from hexlet import fs
# from copy import deepcopy

# # сортировка детей через .reverse()
# tree = fs.mkdir('/', [
#     fs.mkfile('one'),
#     fs.mkfile('two'),
#     fs.mkdir('three', [], {'size': 110}),
# ], {"color": 'red'})

# files = fs.get_children(tree1)
# new_meta = deepcopy(fs.get_meta(tree1))
# new_meta['hidden'] = False
# new_files = files[:]
# new_files.reverse()

# tree2 = fs.mkdir('revers_children', new_files, new_meta)

# print(fs.get_meta(tree2).get('color'))
# print(fs.get_children(tree2))
# print(fs.get_name(tree2))
# print(fs.get_meta(tree2))

# копирование мета-данных
# tree = fs.mkdir('/', [
#     fs.mkfile('one', {'color': 'blue'}),
# ], {"color": 'red'})

# [file]= fs.get_children(tree)
# new_meta = deepcopy(fs.get_meta(file))
# new_meta['hidden'] = True
# new_file = fs.mkfile('aaa', new_meta)

# print(fs.get_meta(new_file))
# print(fs.get_meta(file))
# print(fs.get_name(file))
# print(fs.get_meta(file).get('color'))
# print(fs.is_directory(tree))
# print(fs.is_file(file))


# # Изменение регистра детей с помощью собственной функции
# tree = fs.mkdir('/',[
#     fs.mkfile('One'),
#     fs.mkdir('TwO')
# ])

# # пишем функцию меняющую регистр

# def to_upper(node):
#     name = fs.get_name(node)
#     new_meta = deepcopy(fs.get_meta(node))
#     if fs.is_directory(node):
#         return fs.mkdir(name.upper(), fs.get_children(node), new_meta)
#     return fs.mkfile(name.upper(), new_meta)

# children = fs.get_children(tree)
# new_children = list(map(to_upper, children))# обязательно выражать 
#  # через list()
# new_meta = deepcopy(fs.get_meta(tree)) # ОБЯЗАТЕЛЬНО 
# # ЗАВОДИТЬ НОВУЮ meta

# tree1 = fs.mkdir(fs.get_name(tree), new_children, new_meta)
# # в list загоняется применение fs.get_name() ко всем детям дерева, с помощью map()
# print(list(map(fs.get_name, fs.get_children(tree1))))
# print(list(map(fs.get_name, fs.get_children(tree))))


# # удаление файлов с помощью filter()

# tree = fs.mkdir('/', [
#     fs.mkfile('s'),
#     fs.mkfile('aa'),
#     fs.mkdir('qq')
# ])

# children = fs.get_children(tree)
# new_children = list(filter(fs.is_directory, children))
# new_meta = deepcopy(fs.get_meta(tree))

# tree1 = fs.mkdir(fs.get_name(tree), new_children, new_meta)

# print(list(fs.get_children(tree1)))
# print(list(map(fs.get_name, fs.get_children(tree1))))
# print(list(map(fs.get_name, fs.get_children(tree))))

