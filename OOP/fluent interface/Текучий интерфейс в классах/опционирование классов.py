class Truncater:
    OPTIONS = {
        'separator': '...',
        'length': 200,
    }

    def __init__(self, **options) -> None:
        self.options = {**self.OPTIONS, **options}

    def truncate(self, value, **options):
        current_options = {**self.OPTIONS, **options}
        if len(value) <= current_options['length']:
            return value
        value = value[:current_options['length']] + current_options['separator']
        return value
truncater = Truncater()
print(truncater.truncate('one two')) #== 'one two'
print(truncater.truncate('one two', length=6)) #  == 'one tw...'
print(truncater.truncate('one two', separator='.')) # == 'one two'
print(truncater.truncate('one two', length=3)) # == 'one...'

truncater = Truncater(length=3)
print(truncater.truncate('one two')) #  == 'one...'
print(truncater.truncate('one two', separator='!')) #  == 'one!'
print(truncater.truncate('one two')) #  == 'one...'

print(truncater.truncate('one two', length=7)) # == 'one two'

