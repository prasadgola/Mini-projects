nums = [1,3,4,5,6,3,2]
target = 8
for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i]+nums[j])==target:
            print(i,j)