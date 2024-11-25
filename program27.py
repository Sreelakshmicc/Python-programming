def rectarea(b):
	return lambda l:l*b
def rectper(b):
	return lambda b:2*(l+b)
def squarearea(a):
	return lambda a:a*a
def squarepere(a):
	return lambda a:4*a
print("RECTANGLE")
l=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))
b=rectarea(b)
print("Area is :",b(l))
c=rectper(b)
print("Perimeter is:",c(l))
print("SQUARE")
a=int(input("Enter length of square:"))
z=squarearea(a)
print("Area is:",z(a))
y=squarepere(a)
print("Perimeter is:",y(a))				
