x = -123
l = list(str(x))
p = []
def rotate(l, x):
    return l[-x:] + l[:-x]
for i in range(0,len(l)):
	p.append(l[len(l)-(i+1)])
if p[len(p)-1] == '-':
	q = rotate(p,1)
	print(str(''.join(q)))
else:
	print(str(''.join(p)))