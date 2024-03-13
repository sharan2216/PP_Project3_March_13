# #Method overloading-----------
# # class A:
# #     def meth(a,b):
# #         p=a+b
# #         print(p)
# #
# #     def meth(a,b,c):
# #         p=a+b+c
# #         print(p)
# #
# #
# # obj=A()
# # obj.meth(1,2)
# # obj2=A()
# # obj2.meth(1,2,3)
# #
# #
# # First product method.
# # Takes two argument and print their
# # product
#
#
# def product(a, b):
# 	p = a * b
# 	print(p)
#
# def product(a, b, c):
# 	p = a * b*c
# 	print(p)
#
# product(4, 5)
# product(4, 5, 5)

#Method overriding:==================

class A:
	def meth(self,name):
		self.name=name
		print(f"class A method {self.name}")

class B(A):
	def meth(self,age):
		self.age=age
		print(f"class B method {self.age}")

obj=B()
obj.meth("raj")
obj1=A()
obj1.meth(22)