student={}
Is=[]
n=int(input("Enter the number of students:"))
for i in range(0,n):
	name=input("Enter name:")
	age=input("Enter age:")
	grade=input("Enter grade:")
	student[name]=age,grade
print(student)	
