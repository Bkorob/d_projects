from copy import deepcopy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile

tree1 = mkdir('/', [
    mkfile('one'),
    mkfile('two', {'meta': 'ОЧКО'}),
    mkdir('three', [], {'size': 110}),
], {"color": 'red'})

def change_meta(node, owner):
    name = get_name(node)   # глубокая копия name не нужна, т.к. str - неизменяемый тип данных
    meta = deepcopy(get_meta(node))   # создаём гл.копию meta для последующего изменение
    meta['owner'] = owner   # меняем свойство 'owner'
    if is_file(node):   # точка возврата из рекурсии: если находим файл - возращаем в map() 
        return mkfile(name, meta)   # новый файл с изменённым свойством глубокой копии meta
    
    children = get_children(node)   # если условие не выполнено, - получаем список детей
    new_children = list(map(lambda node: change_meta(node, owner), children))  # создаём новый
    # список детей через map() вызывая себя из lambda: (т.к. у нас 2 аргумента), к полученому 
    # ранее списку детей
    new_meta = deepcopy(get_meta(node))  # делаем глубокую копию meta для всего дерева, чтобы meta
    # директорий не менялась (меняем только свойства файлов)
    new_tree = mkdir(name, new_children, new_meta)  # создаём новое дерево, с созданым рекурсией 
    # списком детей (new_children - c изменённой meta) и глубокой копией основной meta.
    return new_tree   # возвращаем новое дерево
print(change_meta(tree1, 'ХУЙ'))