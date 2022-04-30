import numpy as np
def Place(k,i):
	for x in range(k+1):
		if a[x][i]==1:
			return False
		elif a[k][i]==2:
			return False
		else:
			try:
				if a[k-x][i-x]==1:
					if i-x>=0:
						return False
				elif a[k-x][i+x]==1:					
					return False
			except:
				pass
	return True

def Nqueen(y):
	for qw in range(n):
		if Place(y,qw):
			a[y][qw] =1
			return True
	else:
		return False
possible=[]
def tryS():
	row=1
	while row!=n:
		y=row
		if Nqueen(row):
			row+=1
		else:
			if row-1==0:
				return 0
			else:
				for x in range(n):
					if a[y-1][x]==1:
						a[y-1][x]=2
					else:
						a[y-1][x]==0
				row=row-1
	a[a>1]=0
	possible.append(a)

n = int(input("No. Of Queens: "))
if n<4:
	print("No Possible Outcomes")
else:
	for num in range(n):
		a=np.zeros([n,n])
		a[0][num]=1
		tryS()
	q=1
	for x in possible:
		print(f"\nPossible Solution #{q}")
		for y in x:
			print(y)
		q+=1
