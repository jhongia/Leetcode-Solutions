'''
Jhon Garcia
CS435 Recitation - 12/08/2021

Problem 2:

Given an integer array, find the contiguous subarray 
(containing at least one number) which has the largest 
sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]

Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]

Output: 23
--------------------------------------------------------------------------------
'''

from sys import maxsize
# maxsize() in Python. maxsize attribute of the sys 
# module fetches the largest value a variable of data 
# type Py_ssize_t can store. It is the Python 
# platform's pointer that dictates the maximum size 
# of lists and strings in Python.

def contiguousSubArraySum(nums):
    # Given an integer array, find the contiguous 
    # subarray (containing at least one number) which 
    # has the largest sum and return its sum.
    length = len(nums)
      
    max_curr = -maxsize - 1
    max_end = 0
      
    # Iterate through list
    for i in range(0, length):
        max_end = max_end + nums[i]
        # Compare max curr and end
        if (max_curr < max_end):
            max_curr = max_end
 
        if max_end < 0:
            max_end = 0

    return max_curr

nums = [5,4,-1,7,8]
print("Largest sum is =", contiguousSubArraySum(nums))