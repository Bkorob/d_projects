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
# Функция возращает список пустых дирекоторий с вложенной глубиной не более 1 
def find_empty_dir_paths(tree, depth=0): # глубина считается как 0 на верхнем уровне 
    children = get_children(tree) # получаем список всех детей 
    if len(children) == 0:  # терминальное условие
        return get_name(tree) # если директория пуста то есть детей нет, вернем её имя.
    if depth == 2: # или если глубина равна единице (первый уровень вложенности) 
        return [] # вернём пустой список (убереём его в конце с помощью flatten)
    dir_path = filter(is_directory, children) # получаем только директории
    empty_dirs = list(map(lambda node: find_empty_dir_paths(node, depth + 1), dir_path))# через 
    # рекурсию, с помощью map() и lambda (чтобы передать функцию  с двумя параметрами) передаём 
    # себя, но добавляем +1 к глубине с каждым новым вызовом
    return flatten(empty_dirs) # возращаем результат распечатав его через flatten, чтобы избавиться 
    # от пустых списков

print(find_empty_dir_paths(tree))