def fileRead():

	f=open('C:\\Users\\Shubham\\Desktop\\PythonCodes\\File.txt','r')

	file_data=f.read()
	f.close()
	lst=file_data.split("\n")
	print(file_data)

	print(lst)


fileRead()