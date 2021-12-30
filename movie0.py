l = [0,0,1,2,3]
def shiftit(a):
    l[a] = l[a+1]
    l[a+1] = 0
    return l
for i in range(len(l)-1):
	if l[i] == 0:
		if l[i+1] == 0:
			shiftit(i+1)
		shiftit(i)
print(l)