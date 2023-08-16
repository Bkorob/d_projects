class Truncater:
    def __init__(self, length=200) -> None:
        self.length = length
    def truncate(self, value, length=200, separator='...'):
        self.separator = separator
        if self.length != length:
            self.length = min(length, self.length)
        if len(value) > self.length:
                self.value = value[:self.length] + separator
                return self.value
        self.value = value
        return self.value
    
truncater = Truncater()
# print(truncater.truncate('one two')) #== 'one two'
# print(truncater.truncate('one two', length=6)) #  == 'one tw...'
print(truncater.truncate('one two', separator='.')) # == 'one two'
# print(truncater.truncate('one two', length=3)) # == 'one...'

# truncater = Truncater(length=3)
# print(truncater.truncate('one two')) #  == 'one...'
# print(truncater.truncate('one two', separator='!')) #  == 'one!'
# print(truncater.truncate('one two')) #  == 'one...'

# print(truncater.truncate('one two', length=7)) # == 'one two'

