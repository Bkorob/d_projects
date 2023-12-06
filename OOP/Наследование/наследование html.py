import json
class HTMLElement:
    def __init__(self, attributes=None): # заводим словарь атрибутов(атр:зн)
        self.attributes = attributes if attributes else {}
        self.body = None

    def set_attribute(self, key, value): 
        self.attributes[key] = value

    def get_attribute(self, key): 
        return self.attributes.get(key)

    def set_text_content(self, body): # изменение тела 
        self.body = body

    def get_text_content(self): 
        return self.body

    def stringify_attributes(self): # текстовое представление атрибута(клч-зн)
        return json.dumps(self.attributes)


class HTMLAnchorElement(HTMLElement): # наследуем методы от базового класса и добавляем свой.
    def __str__(self):# базовый тег. автоматически возвращает текстовое представление.
        attr_line = self.stringify_attributes()
        body = self.get_text_content()
        return f'<a{attr_line}>{body}</a>'# возвращаем в текстовом формате
    

anchor = HTMLAnchorElement({'href': '<https://ru.hexlet.io>'})
anchor.set_text_content('Hexlet')
print(f"Anchor: { anchor }")