from itertools import permutations
string,intereger = raw_input().split()
realstr = sorted(string)
realint = int(intereger)
mylist = list(permutations(realstr,realint))
for i in range(len(mylist)):
	print ''.join(mylist[i])