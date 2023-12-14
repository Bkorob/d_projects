# # рекурсивная сумма списка
# def sum(n):
#     if len(n) == 0:
#         return 0
#     return n[0] + sum(n[1:])

# print(sum([1,2,4]))

# # рекурсивный filter
# def f(n):
#     res = []
#     if len(n) == 0:
#         return []
#     if n[0] % 2 == 0:
#         res.append(n[0])
#     res.extend(f(n[1:]))
#     return res
# print(f([1,2,4, 4, 2]))


# рекурсивная замена букв
def swith_volve(ch, sentence):
    if len(sentence) == 0:
        return ''
    if ch in sentence[0]:
        sentence = sentence.replace(ch, '')
    return sentence[0] + swith_volve(ch, sentence[1:])

print(swith_volve('a', 'aba'))

#возращаем  базовый случай, дальше выполняем действие и возращаем базовый случай 
# плюс остальную часть последовательности 