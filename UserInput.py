lst=[12,43,56,12,34,67,89]
set1=set(lst)
lst2=list(set1)
print(lst)
print(lst2)
counter=0
for i in  range(len(lst)):
	for j in range(i,len(lst)):
		if(lst[i]==lst[j]):
			counter+=1
			if(counter>1):
				print(lst[j])
	counter=0

			
