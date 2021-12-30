from collections import defaultdict
n,m=map(int,raw_input().split())
mylist=[]
yourlist=[]
d = defaultdict()
for i in range(n+m):
    if i < n:
        mylist.append(raw_input())
    elif i>=n:
        yourlist.append(raw_input())
for c in mylist:
    d[c]=+1
for i in range(len(yourlist)):
    print d[yourlist[i]]