nom = int(raw_input())
mylist = list(map(int,raw_input().split()))	
ans = all(i > 0 for i in mylist)
l = []
def palindrome(num):
    if num[::-1] == num:
       return True
    else:
       return False
if ans == True:
	for i in range(len(mylist)):
		l.append(palindrome(str(mylist[i])))
	print any(l)
else:
	print False			