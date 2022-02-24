'''
Jhon Garcia
CS435 Recitation - 12/01/2021

Problem 1:

Given an array nums of distinct integers, return all the 
possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]

Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]

Output: [[1]]
--------------------------------------------------------------------------------
'''

def permutation(nums):
    # Given an array nums of distinct integers, return all the 
    # possible permutations. You can return the answer in any order.
    permutations = [[]]

    # Iterate
    for n in nums:
        # Holder list
        perms = []
        for perm in permutations:
            for i in range(len(perm)+1):
                # Add to list of perms
                perms.append(perm[:i] + [n] + perm[i:])
                permutations = perms
    return permutations

nums = [1,2,3]
print(permutation(nums))