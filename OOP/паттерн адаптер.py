import hashlib
from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits as ascii_digits,
    punctuation
)
import random
import re
class PasswordBuilder:
    def init(self, passwordGenerator):
        self.passwordGenerator = passwordGenerator
    def build_password(self, len=10, options=[]):
        password = self.passwordGenerator.generate_password(len, options)
        m = hashlib.sha1()
        m.update(password.encode())
        digest = m.hexdigest()
        return {'password': password, 'digest': digest}
class PasswordGeneratorAdapter:
    def init(self):
        self.generate_password = generate_password
    def generate_password(self, v, option=[]):
        self.options = {
            'uppercase': False,
            'digits': False,
            'symbols': False
        }
        for x in option:
            options[x] = True
        a = self.generate_password(v, self.options)
        return a
def generate_password(len, uppercase=False, digits=False, symbols=False):
    gen_pool = ascii_lowercase
    if uppercase:
        gen_pool += ascii_uppercase
    if digits:
        gen_pool += ascii_digits
    if symbols:
        gen_pool += punctuation
    return ''.join(random.choice(gen_pool) for _ in range(len))


def test_build_password_default_options():
    builder = PasswordBuilder(PasswordGeneratorAdapter())
    password_info = builder.build_password()

    assert len(password_info['password']) == 10


def test_build_password_lowercase():
    builder = PasswordBuilder(PasswordGeneratorAdapter())
    password_info = builder.build_password(12, [])

    assert len(password_info['password']) == 12
    assert password_info['password'].islower()


def test_build_password_uppercase_digits_symbols():
    builder = PasswordBuilder(PasswordGeneratorAdapter())
    password_info = builder.build_password(30, ['uppercase', 'digits', 'symbols'])  # noqa: E501

    assert len(password_info['password']) == 30
    assert re.search(r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).*', password_info['password'])  # noqa: E501


test_build_password_lowercase()