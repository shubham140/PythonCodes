
class Employee:

	def __init__(self,name,age):
		self.name=name
		self.age=age


	def display(self):
		print(self.name)
		print("********************")
		print(self.age)


class My_Class:

	def __init__(self):

		self.msg="We are able to call one class attributes and methods in other class"


	def display(e):
		e.display()




e=Employee("Shubham",24)

m=My_Class
m.display(e)