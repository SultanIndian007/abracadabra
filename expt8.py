print("Naive string Matching DAA Expt 8")
a = str(input("Input String: "))
b= str(input("Pattern String: "))
c=len(b)
l=[]
for x in range(len(a)):
	if a[x:x+c]==b:
		l.append(x+1)
if l!=[]:
	print("\nThe pattern was found at index: ",l)
else:
	print("\nPattern Not Found")
