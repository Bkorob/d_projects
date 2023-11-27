# def get_single(val):
    # name = val.get('name')
    # return f'<{name} class="{val.get("class")}" id="{val.get("id")}">'

def get_pair(val):
    name = val.get("name")
    body = val.get('body', '')
    res = f'<{name}'
    for i,v in enumerate(val.keys()):
        if i > 2:
            res += (f' {v}="{val.get(v, "")}"')
    return res + f'>{body}</{name}>'
    


    return f'<{name} id="{id_}">{body}</{name}>'
# expected = f'<div id="wow" {random_attr}="value">text2</div>'

def stringify(diction):
    actions = {'single': 'get_single',
               'pair': get_pair
        }
    func =  actions[diction.get('tag_type')]
    return func(diction)

tag = {
      'name': 'p',
      'tag_type': 'pair',
      'body': 'text',
    }
tag = {
      'name': 'div',
      'tag_type': 'pair',
      'body': 'text2',
      'id': 'wow',
      'random_attr': 'value',
    }
print(stringify(tag))