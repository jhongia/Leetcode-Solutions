'''
Jhon Garcia
CS435 Recitation - 12/01/2021

Problem 4:

Given an integer array nums of unique elements, return all 
possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]

Output: [[],[0]]
--------------------------------------------------------------------------------
'''

def subsets(nums):
    # Given an integer array nums of unique elements, return all 
    # possible subsets (the power set).
    all_subsets = []

    # Helper function
    rec(all_subsets, nums, [], 0)

    return all_subsets
    
def rec(all_subsets, nums, subset, start):
    all_subsets.append(list(subset))
    
    for i in range(start, len(nums)):
        num = nums[i]
        # Append to list
        subset.append(num)
        # Recursion
        rec(all_subsets, nums, subset, i + 1)
        # Pop element
        subset.pop()

nums = [1,2,3]
print(subsets(nums))