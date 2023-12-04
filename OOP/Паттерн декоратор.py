class InputTag:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def render(self):
        return f'<input type="{self.type}" value="{self.value}">'

    def __str__(self):
        return self.render()

class LabelTag:
    def __init__(self, value, tag):
        self.tag = tag
        self.val = value

    def render(self):
        return f'<label>{self.val}{self.tag.render()}</label>'
    
def test_tags():
    input_tag = InputTag('submit', 'Save')
    label_tag = LabelTag('Press Submit', input_tag)
    expected = '<label>Press Submit<input type="submit" value="Save"></label>'
    assert label_tag.render() == expected
    assert str(label_tag) == expected
print(test_tags())