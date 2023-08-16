def gen_diff(array1, array2):
    # added = set(array2.keys() - array1.keys())
    unchanged = set(x[0] for x in set(array1.items() & array2.items()))
    deleted = set(array1.keys() - array2.keys())
    changed = set(
        x for x in set(array1.keys() & array2.keys()) if array1[x] != array2[x]
                  )
    mores = set(tuple(array2.keys()) + tuple(array1.keys()))
    ended_values = dict()
    for x in mores:
        if x in unchanged:
            ended_values[x] = "unchanged"
        elif x in deleted:
            ended_values[x] = 'deleted'
        elif x in changed:
            ended_values[x] = 'changed'
        else:
            ended_values[x] = 'added'
    return ended_values
    
    
print(gen_diff(
    {"one": "eon", "two": "two", "four": True},
    {"two": "own", "zero": 4, "four": True},
))

# {"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}
