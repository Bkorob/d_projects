from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
 # ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ: функция считает числовые значения параметра 'size' в meta файлов
def get_sum_files(node):
    meta = get_meta(node) # получаем meta в переменную
    if is_file(node):
        return meta['size'] # точка выхода: возврат свойства меты 'size', если нашли файл
    children = get_children(node) # если нет: формируем список детей
    result = list(map(get_sum_files, children)) # записываем в переменную результат рекурсивного применения
    # функции к списку детей.
    return sum(result) # возращаем сумму полученных вычислений 

# ОСНОВНАЯ ФУНКЦИЯ: возвращает отсортированный список кортежей с именем и размером каждой из директорий
# содержащих файлы с нужным пораметром.
def du(node):
    children = get_children(node) # получаем список детей
    result = list(map( # используя map(), с помощью lambda(), которая даёт возможность      
        lambda node: (get_name(node), get_sum_files(node)), # использовать через кортеж две функции,
        children))  # вместо одной, записываем в результат получение имени узла и применение фунции 
    # get_sum_files()  к списку детей. Она внутри себя рекурсивно производитт все вычисления
    result.sort(key=lambda file: file[1], reverse=True) # сортирум по второму параметру 
    return result # возращаем отсортированный результат.

print(du(tree))