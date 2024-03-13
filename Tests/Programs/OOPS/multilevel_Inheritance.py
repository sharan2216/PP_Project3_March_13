class Person:
    def __init__(self,name,age,sal):
        self.name=name

    def display(self):
        print(f'name is {self.name}')


class P1(Person):
    def __init__(self, name,age,sal):
        super().__init__(name,age)
        self.sal = sal

    def display(self):
        print(f'name is {self.name} age is {self.age} ')


class P2(Person):
    def __init__(self, name,age,sal):
        super().__init__(name,age,sal)
        self.sal = sal

    def display(self):
        print(f'name is {self.name} age is {self.age} and salary is {self.sal}')


obj=Person("Raj",20000,21)
obj.display()
obj1=P1
obj1.display()
obj2=P2
obj2.display()
