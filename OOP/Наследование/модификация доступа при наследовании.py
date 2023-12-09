class HTMLElement:
    def __init__(self, attributes=None):
        if attributes is None:
            self.attributes = {}
        self.attributes = attributes

    def get_attribute(self, key):
        return self.attributes.get(key)

    # BEGIN (write your solution here)
    def _reorg(self, data):
        if type(data) is str:
            return data.split(' ')
        return ' '.join(data)
    
    def get_all(self, data):
        for x in data.keys():
            return x, self._reorg(self.get_attribute(x))

    def add_tag(self, tag):
        key, values = self.get_all(self.attributes)
        if tag not in values:
            values.append(tag)
        self.attributes[key] = self._reorg(values)
        return self.attributes

    def remove_tag(self, tag):
        key, values = self.get_all(self.attributes)
        values.remove(tag)
        self.attributes[key] = self._reorg(values)

    def toggle_tag(self, tag):
        values = self.get_all(self.attributes)[1]
        if tag in values:
            return self.remove_tag(tag)
        return self.add_tag(tag)
    # END

class HTMLDivElement(HTMLElement):
    pass


def test_HTMLDivElement():
    tag = 'one two'
    div = HTMLDivElement({'tag': tag})
    assert div.get_attribute('tag') == tag

    div.add_tag('small')
    assert div.get_attribute('tag') == 'one two small'

    div.add_tag('small')
    assert div.get_attribute('tag') == 'one two small'

    div.remove_tag('two')
    assert div.get_attribute('tag') == 'one small'

    div.toggle_tag('small')
    assert div.get_attribute('tag') == 'one'

    div.toggle_tag('small')
    assert div.get_attribute('tag') == 'one small'


print(test_HTMLDivElement())