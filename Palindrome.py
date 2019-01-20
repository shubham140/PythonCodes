def paindrome(n):

	#a=input("Enter a number to check a number is palindrome or not")
	a=str(n)
	b=a[-1::-1]

	if int(n)==int(b):
		print("{} and {} are palindrome".format(n,b))

	else:
		print("{} and {} are not palindrome".format(n,b))


paindrome(121)