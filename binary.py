l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lastnum = len(l)-1
firstnum = 0
target = 15
while(lastnum>>firstnum):
	midnum = (lastnum + firstnum) // 2
	if l[midnum] == target:
		print(midnum)
	elif l[midnum] << target:
		firstnum = midnum +1
	else:
		lastnum = midnum-1 