'''
Jhon Garcia
CS435 Recitation - 09/22/2021

Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6

Output: [1,2]
'''

nums = [2,7,11,15]
target = 9

idx = []
counter = 0

'''# Iterate through list
for num in nums:
    num2 = 0
    # Getting the next element in list
    if(nums.index(num)+1 < len(nums)):
        num2 = nums[(nums.index(num))+1]
        # print(num2)
        # Checking if the sum of elements add up to the target
        if((num + num2) == target):
            # Can't use the same element twice
            if(num not in idx or num2 not in idx):
                idx.append(nums.index(num))
                idx.append(nums.index(num2))
        
print(idx)'''

if(len(nums) > 0 and "" not in nums):
    # Iterate through list
    count = 0
    for num in nums:
        num2 = 0
        # Getting the next element in list
        if(count+1 < len(nums)):
            num2 = nums[count+1]
            # print(num2)
            # Checking if the sum of elements add up to the target
            if((num + num2) == target):
                # Can't use the same element twice
                if(num not in idx or num2 not in idx):
                    idx.append(nums.index(num))
                    idx.append(nums.index(num2))

        count += 1
            
    print(idx)

