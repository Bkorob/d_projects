class BankAccount:
    '''Создайте класс BankAccount, у которого будет свойство balance (баланс счета). 
    Реализуйте методы для получения и установки значения свойства 
    balance с использованием декоратора @property. 
    Реализуйте также методы для пополнения и снятия денег со счета.'''
    def __init__(self) -> None:
        self._balance = 0 

    def get_balance(self):
        return f'{self._balance}$'
    
    def set_balance(self, value):
        if value < 0:
            raise ValueError
        self._balance = value

    def withdraw_money(self, val):
        self._balance -= abs(val)
        if self._balance < 0:
            raise ValueError('столько снять нельзя')

    def put_money(self, val):
        self._balance += abs(val)

    balance = property(fget=get_balance, fset=set_balance)



c1 = BankAccount()
print(c1.balance)
c1.balance = 1000
c1.withdraw_money(300)
print(c1.balance)
c1.put_money(300)
print(c1.balance)



        