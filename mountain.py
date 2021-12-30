l  = [1,2,3,4,5,4,6,2,5,1]
n = 0
for i in range(len(l)-1):
	if l[i] <= l[i+1]:
		n = 0
	elif l[i]>>l[i+1]:
		n = 1

