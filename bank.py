class bank:
	def __init__(self,accno,name,acct,bal):
		self.accno=accno
		self.name=name
		self.acct=acct
		self.bal=0
	def showamt(self):
		print("Account Holder Name:",self.name)
		print("Account Number:",self.accno)
		print("Account Type:",self.acct)
		print("Your Balance Amount:",self.bal)
	def depo(self,d1):
		self.bal=self.bal+d1
		return self.bal
	def withd(self,w1):
		self.bal=self.bal-w1
		return self.bal
n = input("Enter your name: ")
a = int(input("Enter your Account number: "))
t = input("Enter your account type: ")
o=bank(a,n,t,bal=0)
o.showamt()
while(True):
	print("\n Menu")
	print("Enter 1 for Deposit")
	print("Enter 2 for Withdraw")
	print("Enter 3 for Details")
	c=int(input("Enter Your Choice:"))
	if(c==1):
		d=int(input("\nEnter the amount to deposit :"))
		print("Your total balance is :",o.depo(d))
	elif(c==2):
		w=int(input("Enter the amount to withdraw :"))
		if(w>o.bal):
			print("INSUFFICIENT BALANCE")
		else:
			print("Your total balance is :",o.withd(w))
	elif(c==3):
		o.showamt()
	else:
		print("Enter a valid choice")
