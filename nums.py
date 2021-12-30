nums = [1,1,2]

if len(nums) >= 3:
            nums = list(set(nums))
            nums.remove(max(nums))
            nums.remove(max(nums))
            print (max(nums))
else:
    print (max(nums))