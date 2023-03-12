import os

from hexlet.fs import flatten, get_children, get_name, is_file, mkdir, mkfile

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])

# ИСПОЛЬЗУЕМ АККУМУЛЯТОР ДЛЯ НАКОПЛЕНИЯ ДАННЫХ, В МОМЕНТ ОБХОДА ФУНКЦИИ
def find_files_by_name(tree, string):
    def walk(node, path): # вложенная функция принимает текущий узел и переменную начала пути
        name = get_name(node) # получаем имя узла
        acc = os.path.join(path, name) # аккумулятор - сохраняет часть пути до узна на текущий 
        # момент, путём склеивания начала пути(path) и текущего имени узла
        if name.find(string) > -1 and is_file(node): # условие выхода, если у нас файл, содержащий
        # часть строки, возращаем путь до него
            return acc
        children = get_children(node) # если нет, получаем потомков 
        path_list = list(map(lambda node: walk(node, acc), children)) # рекусивно, через map(),
        # применяем к потомкам себя(посредством lambda, чтобы передать функцию с 2мя параметрами)
        # вторым параметром передаём аккумулятор, как базовый путь, чтобы он сохранялся в path
        return flatten(path_list) # возращаем полученный результат, предварительно убрав 
        # все пустые списки. 
    return walk(tree, '') # возращаем вложенную функцию, с пустым начальным путём, чтобы было 
    # окуда начинать.
    
print(find_files_by_name(tree, 'co'))