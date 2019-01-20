class 	Person:

	def __init__(self):
		self.name="shubham"
		self._age=24
		self.__sex="m"

	def method(self):
		print(self.name)
		print(self._age)
		print(self.__sex)



p=Person()
p.method()
print(p._age)
print(p._Person__sex) # This right here known as name mangling which is done when we have to access private attributes of class outside of class....