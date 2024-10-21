def add(n1,n2):
	return n1+n2
def subtract(n1,n2):
	return n1-n2
def multiplication(n1,n2):
	return n1*n2
def division(n1,n2):
	return n1/n2
def power(n1,n2):
	return n1**n2
def calculator(n1,op,n2):
	if op=="+":
		return add(n1,n2)
	elif op=="-":
		return subtract(n1,n2)
	elif op=="*":
		return multiplication(n1,n2)	
	elif op=="/":
		return division(n1,n2)	
	elif op=="**":
		return power(n1,n2)	
	else:
		print("Invalid Syntax")
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
op=input("Enter any operation:\n+ \n- \n* \n/ \n**\n")
result=calculator(n1,op,n2)
print("Result is:",result)			
			
														
									
							
