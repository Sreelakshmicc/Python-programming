def is_palindrome(n):
	n_rev=n[::-1]
	if n==n_rev:
		return True
	else:
		return False
n=input("Enter a string:")
result=is_palindrome(n)
if result==True:
	print("Palindrome")
else:
	print("Not a palindrome")				
