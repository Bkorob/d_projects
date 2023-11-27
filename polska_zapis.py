import operator
get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}.get


def rpn_calc(rpn):
    stack = []
    for elem in rpn:
        op = get_operator(elem)
        if op is not None:
            x = stack.pop()
            y = stack.pop()
            elem = op(y, x)
        stack.append(elem)
    return stack[0]
            
            
print(rpn_calc([7, 2, 3, '*', '-']))



Python 3.11.6 (main, Oct  8 2023, 05:06:43) [GCC 13.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.17.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: assert True

In [2]: assert False
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
Cell In[2], line 1
----> 1 assert False