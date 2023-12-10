class HTMLElement:
    def __init__(self, attributes=None):
        self.attributes = attributes if attributes else {}

    def _stringify_attributes(self):
        print(self.attributes.items())
        line = ''.join(f' {k}="{v}"' for k, v in self.attributes.items())
        return line
    

class HTMLPairElement(HTMLElement):
    def __init__(self, attributes=None):
        super().__init__(attributes)
        self.body = ''

    def get_text_content(self):
        return self.body if self.body else ''

    def set_text_content(self, text):
        self.body = text

    def __str__(self):
        attr = super()._stringify_attributes()
        body = self.get_text_content()
        name = self.get_tag_name() # момент определения шаблона для класса наследника
        # класс наследник должен иметь такой метод
        return f'<{name}{attr}>{body}</{name}>' # применение в коде. родитель не знает 
        # как реализован шаблон
    

class HTMLDivElement(HTMLPairElement): # реализация шаблона
    def get_tag_name(self):
        return 'div'