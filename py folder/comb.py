from itertools import combinations
stri,size = raw_input().split()
string1 = sorted(stri)
intsize = int(size)
main = list(combinations(string1,intsize))
for j in range(len(string1)):
	print string1[j]
for i in range(len(main)):
	print ''.join(main[i])
