nums = [-1, 0, 1, 2, -1, -4]
matrix = []
for i in range(len(nums)):
	for j in range(len(nums)):
		for k in range(len(nums)):
			if (nums[i]+nums[j]+nums[k]==0):
				matrix.append([nums[i],nums[j],nums[k]])
print(matrix[0,1])