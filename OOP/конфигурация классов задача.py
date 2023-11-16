class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }
    # BEGIN (write your solution here)

    def __init__(self, **options):
        self.config = self.OPTIONS | options

    def _has_number(self, password):
        return any(char.isdigit() for char in password)

    def validate(self, password):
        out = {}
        if len(password) < self.config['min_len']:
            out['min_len'] = 'too small'
        if self.config['contain_numbers']:
            if not self._has_number(password):
                out["contain_numbers"] = 'should contain at least one number'
        return out