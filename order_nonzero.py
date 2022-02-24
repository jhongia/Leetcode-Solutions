'''
Jhon Garcia
CS435 Recitation - 10/06/2021

Problem 1:

Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]

Output: [1,3,12,0,0]

Input: nums = [0]

Output: [0]
'''

nums = [0,0,1,0,3,0,12]
print(nums)

for num in nums:
    if(num == 0):
        # pop number from list then append to the
        nums.append(nums.pop(nums.index(num)))

print(nums)
