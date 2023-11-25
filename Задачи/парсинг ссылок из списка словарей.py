def get_links(arg):
    return [val[1] for val in [
        [dicts.get(link) for link in dicts] for dicts in arg] if val[0] in[
            'img', 'link', 'a']]
                
                
    
tags = [
        {'name': 'p'},
        {'name': 'a', 'href': 'hexlet.io'},
        {'name': 'img', 'src': 'hexlet.io/assets/logo.png'},
    ]
 
print(get_links(tags))