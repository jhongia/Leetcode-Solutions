'''
Jhon Garcia
CS435 Recitation - 10/13/2021

Problem 2: 

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
 
Input: nums = [3,0,1]

Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Bonus Point : Could you implement a solution using only O(1) extra space 
complexity and O(n) runtime complexity?
'''

nums = [3,0,1]

range = list(range(0,len(nums)+1))

for num in range:
    if num not in nums:
        print(num)



