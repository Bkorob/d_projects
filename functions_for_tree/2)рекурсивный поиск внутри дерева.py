import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile



tree = mkdir('/',[
    mkdir('etc',[
    mkfile('bashrc'),
    mkfile('consul.cfg')
    ]),
    mkfile('hexletrc'),
    mkdir('bin',[
    mkfile('lc'),
    mkfile('cat')
    ])
])
def dfs(node):
    print(get_name(node))

    if is_file(node): # возращаемся из функции, если нашли файл
        return
    
    children = get_children(node)
    list(map(dfs, children))

dfs(tree)
# /
# etc
# bashrc
# consul.cfg *ЗДЕСЬ dfs() ВОЗРАЩАЕТ УПРАВЛЕНИЕ map(), КОТОРАЯ СНОВА ПРИМЕНЯЕТ ЕЁ К ПЕРЕМЕННОЙ children
# hexletrc *ЗДЕСЬ dfs() ВОЗРАЩАЕТ УПРАВЛЕНИЕ map(), КОТОРАЯ СНОВА ПРИМЕНЯЕТ ЕЁ К ПЕРЕМЕННОЙ children
# bin
# lc
# cat *КОНЕЦ ДЕРЕВА

#print(list(map(get_name, get_children(tree))))