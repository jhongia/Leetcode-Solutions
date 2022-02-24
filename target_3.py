'''
Jhon Garcia
CS435 Recitation - 10/27/2021

Problem 3:

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6],

target = 5

Output: 2

------------------------------------------------------------

Example 2:

Input: nums = [1,3,5,6],

target = 2

Output: 1

------------------------------------------------------------

Example 3:

Input: nums = [1,3,5,6],

target = 7

Output: 4

------------------------------------------------------------

Example 4:

Input: nums = [1,3,5,6],

target = 0

Output: 0
'''
 
def inserted_index(nums, l, target):
    # Function to find index

    # Check all elements 
    for i in range(l):
         
        # target found return i
        if nums[i] == target:
            return i
             
        # if num is greater than target return i
        elif nums[i] > target:
            return i
             
    # if elements are smaller then return l
    return l

nums = [1,3,5,6]
l = len(nums)
target = 7

print(inserted_index(nums, l, target))