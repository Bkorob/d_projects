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
            data =  data.split(' ')
            return data
        data = ' '.join(data)
        return data

    def add_tag(self, tag):
        for x in self.attributes.keys():
            first = self._reorg(self.get_attribute(x))
            first.append(tag)
            self.attributes[x] = self._reorg(first)
            return self.attributes

    def remove_tag(self, tag_name):
        pass

    def toggle_tag(self, tag_name):
        pass
    # END

class HTMLDivElement(HTMLElement):
    pass


tag = 'one two'
div = HTMLDivElement({'tag': tag})
div.add_tag('small')
print(div.get_attribute('tag')) #== 'one two small'

# # def test_HTMLDivElement():
#     tag = 'one two'
#     div = HTMLDivElement({'tag': tag})
#     assert div.get_attribute('tag') == tag

#     div.add_tag('small')
#     assert div.get_attribute('tag') == 'one two small'

#     div.add_tag('small')
#     assert div.get_attribute('tag') == 'one two small'

#     div.remove_tag('two')
#     assert div.get_attribute('tag') == 'one small'

#     div.toggle_tag('small')
#     assert div.get_attribute('tag') == 'one'

#     div.toggle_tag('small')
#     assert div.get_attribute('tag') == 'one small'