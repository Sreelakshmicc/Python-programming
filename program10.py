def sum_of_first_n(n):
	sum=0
	for i in range(1,n+1):
		sum+=i
	return sum
n=int(input("Enter a number:"))
result=sum_of_first_n(n)
print("The sum of first",n,"number is:")
print(result)			
