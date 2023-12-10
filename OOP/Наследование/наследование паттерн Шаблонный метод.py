class A:
    def build(self, val):
        self.val = val
        value = self.get_val_attr(val)
        return self.val + value
    

class B(A):
    def get_val_attr(self, val):
        return val[::-1]
    

a = B()

print(a.build('хуй'))
