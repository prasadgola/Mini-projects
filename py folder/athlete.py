n,m = map(int,raw_input().split()
mylist = []
for i in range(n):
    mylist.append(map(int,raw_input().split()))
k = int(raw_input())
newlist = zip(*mylist)
l = sorted(newlist[k])
for e in range(len(l)):
    for w in range(len(mylist)):
        if l[e] == mylist[w][k]:
            print ' '.join(map(str, mylist[w]))