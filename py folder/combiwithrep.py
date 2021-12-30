from itertools import combinations_with_replacement
string1,integer = raw_input().split()
mystr = sorted(string1)
realint = int(integer)
mylist = list(combinations_with_replacement(mystr,realint))
for i in range(len(mylist)):
	print ''.join(mylist[i])