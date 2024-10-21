string=input("Enter the string: ")
count=0
for i in range(0,len(string)): 
	if string[i]!='':
		count+=1
print("The number of characters are:",count)		
