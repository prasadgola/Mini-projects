n = int(input())
a=[]
for i in range(0,n):
	y=input().split(' ')
	if y[0]== 'insert':
		a.insert(int(y[1]),int(y[2]))
	elif y[0]=='print':
		print(a)
	elif y[0]=='remove':
		a.remove(int(y[1]))
	elif y[0]=='append':
		a.append(int(y[1]))
	elif y[0]=='sort':
		a.sort()
	elif y[0]=='pop':
		a.pop()
	elif y[0]=='reverse':
		a.reverse()			