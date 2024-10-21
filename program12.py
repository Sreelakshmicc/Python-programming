print("Enter the binary number:",end="")
binary_num=int(input())
decimal_num=0
m=1
binarylen=len(str(binary_num))
for i in range(binarylen):
	remainder=binary_num%10
	decimal_num=decimal_num+(remainder*m)
	m=m*2
	binary_num=int(binary_num/10)
print("Equivalent decimal value:",decimal_num)	
