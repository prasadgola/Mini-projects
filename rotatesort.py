lis = [1,3,4,5,8,12,15,17,19,23,26]
target = 23
u = 0
l = len(lis)-1
while(l>=u):
    mid = (u+l)//2
    if lis[mid] == target:
    	print(lis.index(lis[mid]))
    	break
    elif target < lis[mid]:
    	l = mid-1
    else:
    	u = mid+1