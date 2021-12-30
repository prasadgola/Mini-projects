x = str(321-)
l = list(x)
u = []
e = ''
for i in range(0,len(l)):
	u.insert(i,l[len(l)-(i+1)])
	u[i] = str(u[i])
y = e.join(u)
print (y)