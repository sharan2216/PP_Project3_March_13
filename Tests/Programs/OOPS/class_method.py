class Employee:
    company_name="infosys"

    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    @classmethod
    def get_company(cls):
        print(f"company name is:",cls.company_name)

a1=Employee("Raj",100000)
a2=Employee("rohan",200000)
print(a1.sal)
print(a1.name)
print(a1.company_name)
a1.get_company()

Employee.get_company()

