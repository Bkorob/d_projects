class Truncater:
    OPTIONS = {
            'separator': '',
            'length': 200,
               }

    def __init__(self, **opt):
        self.options = self.OPTIONS | opt

    def truncate(self, text, **option):
        self.setup = self.options | option
        if len(text) <= self.setup['length']:
            return text
        self.result = text[:self.setup['length']] + self.setup['separator']
        return self.result


truncater = Truncater()
print(truncater.truncate('one two', separator='.', length=3))
print(truncater.truncate('one two', length=6))

