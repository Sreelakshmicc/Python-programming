def fibonacci(n):
	if n==0 or n==1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the number:"))
print("Fibonacci numbers are:")
for i in range(n):
	print(fibonacci(i),end="\n")			
