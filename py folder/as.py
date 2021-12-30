from collections import defaultdict
name = "IndianPythonista"
d = defaultdict(int)
for c in name:
	d[c]=+1
print d['z']