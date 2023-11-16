class Collection: #возврат вместо нового экземпляра определенного класса
    def __init__(self, coll):
        self.coll = coll

    def map(self, fn): # экземпляра dunder-метода __class__
        return self.__class__(list(map(fn, self.coll)))
    
    def filter(self, fn): # он всегда указывает на экземпляр именно ТЕКУЩЕГО класса
        return self.__class__(list(filter(fn, self.coll)))
    
    def all(self): # в остальном ничем не отличается от возврата экземпляра
        # конкретного класса
        return self.coll