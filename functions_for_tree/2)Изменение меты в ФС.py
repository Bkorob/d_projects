import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)
def compress_images(node):
    children = get_children(node) # заводим в переменную список детей
    
    def to_fix_meta(node): # создаём функцию для обработки meta узла
        name_ch = get_name(node) # получаем имя узла
        if name_ch.endswith('.jpg') and is_file(node): # заводим условие
            new_meta = copy.deepcopy(get_meta(node)) # при верном условии, в глубокой копии meta делим значение 
            new_meta['size'] //= 2 # ключа пополам 
            return mkfile(name_ch, new_meta) # возращаем новый файл с полученным ранее именем и отредактированной 
                                           # копией meta
        return node # если условие не выполнено: - возращаем узел неизменённым
    
    new_children = list(map(to_fix_meta, children)) # заводим новый список детей путём применения созданной функции
                                                    # ко всем элементам ранее созданного списка детей, через map()
    new_meta = copy.deepcopy(get_meta(node)) # делаем глубокую копию meta, чтобы она не конфликтовала с
                                             # ранее изменёнными meta-данными
    
    return mkdir(get_name(node), new_children, new_meta) # возращаем новое дерево

tree = mkdir(
    'my documents',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)
print(compress_images(tree))