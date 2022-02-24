'''
Jhon Garcia
CS435 Recitation - 10/20/2021

Problem 4:

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

Input: nums = [1,2,3,1]

Output: 2

3 is a peak element and your function should return the index number 2.

Input: nums = [1,2,1,3,5,6,4]

Output: 5

Explanation: Your function can return either index number 1 where the peak 
element is 2, or index number 5 where the peak element is 6.
'''

def Peak(nums, k) :
 
    # first or last element is peak
    if (k == 1):
        return 0

    if (nums[0] >= nums[1]):
        return 0

    if (nums[k - 1] >= nums[k - 2]):
        return k - 1
  
    # check for the rest of elements
    for i in range(1, k - 1) :
  
        # check if any neighbor is smaller
        if (nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]):
            return i
             
nums = [1,2,1,3,5,6,4]
k = len(nums)
print(Peak(nums, k))