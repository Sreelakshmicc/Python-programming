y={"Megha":1,"Riya":2,"Siya":3}
l=list(y.items())
l.sort()
print("Ascending order is:",l)
l=list(y.items())
l.sort(reverse=True)
print("Descending order is:",l)
dict=dict(l)
