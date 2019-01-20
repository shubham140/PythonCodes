class Person:

	def __init__(self,name,age):

		self.name=name
		self.age=age


	def display(self):
		print(self.name)
		print(self.age)



	class Dob:

		def __init__(self,dd,mm,yy):
			self.dd=dd
			self.mm=mm
			self.yy=yy

		def display(self):

			print("{}/{}/{} is date of birth".format(self.dd,self.mm,self.yy))




p=Person("Shubham",24)
p.display()

x=Person("shubham",24).Dob(10,2,1994)
x.display()