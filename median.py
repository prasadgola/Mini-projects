l = [1,2,3,4]
u = [5,6,7]
j = list(set(l+u))
p = len(j)//2
if len(j)%2!=0:
	print(j[len(j)//2])
else:
	print((j[p]+j[p+1])/2)
#print(len(j))