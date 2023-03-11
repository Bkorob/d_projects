from copy import deepcopy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile

tree1 = mkdir('/', [
    mkfile('zero'),
    mkfile('one'),
    mkfile('two', {'meta': 'ОЧКО'}),
    mkdir('three', [], {'size': 110}),
], {"color": 'red'})

def get_count_tree(node):
    if is_file(node):
        return 1 # терминальная стадия выхода их алгоритма(точка выхода)
    
    children = get_children(node) # если не выполнена терминалка, формируем в переменную список детей
    count = list(map(get_count_tree, children)) # в переменной формируем, в списке через map() 
    #                                           вызов себя для списка детей
    return sum(count) # возращаем сумму элементов получившегося списка

print(f'Всего папок: {get_count_tree(tree1)}')
# Подсчёт всех папок и файлов
def counting_all_elemets(node):
    if is_file(node):
        return 1 # терминалка 
    children = get_children(node) # если не терминалка, то формируем список детей 
    all_count = list(map(counting_all_elemets, children)) # екурсивно вызываем себя через map() к списку детей
    return 1 + sum(all_count) # возразаем единицу(текущая директория) и сумму списка all_count в 
    # который рекурсивно попадает количество файлов

print(f'Всего папок и файлов: {counting_all_elemets(tree1)}')
