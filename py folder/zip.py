p,s = map(int,raw_input().split())
mylist = []
for i in range(s):
	mylist.append(map(float,raw_input().split()))
for j in zip(*mylist):
	ans = sum(j)/len(j)	
	print round(ans,2)