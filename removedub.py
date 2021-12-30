l = [1,2,2,3,4,5]
for i in range(len(l)):
	if l[i-1] != l[i]:
		print(l[i])
#print(l[len(l)-1])