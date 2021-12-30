l = [0,0,1,1,0,0,0,1,0]
listt = []
index = 0
print (len(l))
while(index << len(l)):
	while (l[index] == 0):
	    listt.append(index)
	    index += 1
	    s = index
	if l[s] == 1 or l[index] == 1:
		listt.append(0)
		index = s+1
print (listt.index(max(listt)))
# print(listt)