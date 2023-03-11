from copy import deepcopy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile, is_directory

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf'),
        ]),
    ]),
    mkdir('consul', [
        mkfile('config.json'),
        mkfile('file.tmp'),
        mkdir('data'),
    ]),
    mkfile('hosts'),
    mkfile('resolve'),
])
#Считаем количество файлов напрямую
def counting_dir(node):
    if is_file(node):
        print(get_name(node))
        return 1
    print(get_name(node))
    children = get_children(node)
    count_ch = list(map(counting_dir, children))
    return 1 + sum(count_ch)

#print(counting_dir(tree))

def get_subderictories_info(node):
    children = get_children(node)
    #filtred_dir = filter(is_directory, children)

    dir_info = list(map(lambda node: (get_name(node), counting_dir(node)),
                        children,
                        ))
    return dir_info

print(get_subderictories_info(tree))