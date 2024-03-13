class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def set_method(self):
        return self.a+self.b

    def get_method(self):
        print(self.a+self.b)



obj=A(3,5)
obj.set_method()
obj.get_method()