l = [1,2,3,5]
target = 4
if target in l:
 	print(l.index(target))
else:
 	l.append(target)
    setnums = list(set(l))
    print(setnums.index(target))