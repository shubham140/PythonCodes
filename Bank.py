class Bank:

	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance



	def depoist(self,amount):

		self.balance+=amount
		print("The depoist is successful with {} amount".format(amount))
		print("Current balance is{}".format(self.balance))


	def withdrawl(self,amount):

		if(amount<=self.balance):
			self.balance-=amount
			print("the withdrawl is successful.")

			print("Current bank balance is {}".format(self.balance))





b=Bank("RAJU",234567)

print("w-Withdrawl d-Depoist e-Exit")
a=input("Enter the action")

if(a=="w"):
	amount=int(input("Enter the amount"))
	b.withdrawl(amount)
elif(a=="d"):
	amount=int(input("Enter the amount"))
	b.depoist(amount)
elif(a=="e"):
	sys.exit()
	print("Thankyou")



