
def sort(sentence, r=' ') -> str:
    list_ = sentence.split(r)
    res =  []
    for x in list_:
        if x[0].istitle():
            res.append(''.join(sorted(x.lower())).capitalize())
        elif "'" in x:
            res.append(sort(x, "'"))
        elif "-" in x:
            res.append(sort(x, "-"))
        else:
            if x.endswith('.'):
                x = x[:-1]
                res.append(''.join(sorted(x))+'.')
            elif x.endswith(','):
                x = x[:-1]
                res.append(''.join(sorted(x))+',')
            else:
                res.append(''.join(sorted(x)))
    return ' '.join(res)

print(sort("This challenge doesn't seem so hard."
))