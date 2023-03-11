from hexlet.fs import get_children, get_meta, get_name, flatten, mkdir, mkfile, is_directory 


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf'),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkdir('data'),
        ]),
    ]),
    mkdir('logs'),
    mkfile('hosts'),
])

# Функция возращает только пусные директории налюбой губтне вложенности
def find_empty_dir_paths(tree): 
    children = get_children(tree) # получаем список детей для перерменной children
    if len(children) == 0: # терминальное условие: если список пустой, 
        return get_name(tree) # возращаем имя узла.
    dir_names = [x for x in children if is_directory(x)] # если список детей не пустой 
    # заводим в переменную только директории (можно сделать с помощью filter(is_directory, children)). 
    empty_dir = list(map(find_empty_dir_paths, dir_names)) # рекурсивно применяем функцию к отсортироанному
    # списку детей
    return flatten(empty_dir) # возращаем результат. flatten - убирает лишние уровни вложенности,
    # так как функция возращает список на каждом уровне вложенности.

    
print(find_empty_dir_paths(tree))

