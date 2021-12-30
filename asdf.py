nums = [0,0,1,1,1,2,3,3,3,4]
u = set()	
for i in range(0,len(nums)):
	u.add(nums[i])
u = list(u)
print(u)