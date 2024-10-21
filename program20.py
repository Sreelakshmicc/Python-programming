a=[]
n=int(input("Enter the number of elements:"))
for x in range(0,n):
	element=input("Enter the element "+str(x+1)+":")
	a.append(element)
max=len(a[0])
temp=a[0]
for i in a:
	if(len(i)>max):
		max=len(i)
		temp=i
print("The longest word is:")
print(temp)	
	
