import re
# подумать про использование стека и FIFO для хранения выражений в скобках 
def parse_molecule(form):
    sol_space = [[]]
    pr = []
    lst_molecules = re.findall('[A-Z][a-z]?|\d+|.', form)
    for i in range(len(lst_molecules)):
        if lst_molecules[i].isalpha():
            subst = [lst_molecules[i]]
        elif lst_molecules[i].isdecimal():
            count = int(lst_molecules[i])
            sol_space[-1].extend(count * subst)
        elif lst_molecules[i] in '[{(':
            while lst_molecules[i] not in ']})':
                pr.append(lst_molecules[i])
                i+=1
                
                
                
        # elif lst_molecules[i] in ']})':
        #     subst = sol_space.pop()
        #     sol_space.extend(subst)                    
    return sol_space
    
    
# from collections import Counter

# def parse_molecule(molecule):

#     array = [[]]

#     for token in map(str, molecule):
#         if token.isalpha() and token.istitle():
#             last = [token]
#             upper = token
#             array[-1].append(token)
#         elif token.isalpha():
#             last = upper + token
#             array[-1] = [last]
#         elif token.isdigit():
#             array[-1].extend(last*(int(token)-1))
#         elif token == '(' or token == '[':
#             array.append([])
#         elif token == ')' or token == ']':
#             last = array.pop()
#             array[-1].extend(last)

#     return array[-1]
print(parse_molecule("K4[ON(SO3)2]2"))