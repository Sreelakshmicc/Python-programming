input_str = input("Enter the list elements:\n")   
list_num = input_str.split()  
list_num = [int(num) for num in list_num]  
for i,v in enumerate(list_num):
	list_num[i] = v**2
print("The square is:",list_num)
