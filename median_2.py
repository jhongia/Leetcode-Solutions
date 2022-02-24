'''
Jhon Garcia
CS435 Recitation - 11/10/2021

Problem 2:

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]

Output: 2.00000

Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]

Output: 2.50000

Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]

Output: 0.00000 

Example 4:

Input: nums1 = [], nums2 = [1]

Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []

Output: 2.00000
'''

def getSortedMedian(nums1, nums2):
    # Get Median of two sorted arrays

    ln1 = len(nums1)
    ln2 = len(nums2)

    # curr index nums1
    i = 0 

    # curr index nums2
    j = 0

    # holders
    x1, x2 = -1, -1

    # if n+m is odd then middle index is median
    if((ln2 + ln1) % 2 == 1):   
        for count in range(((ln1 + ln2) // 2) + 1):       
            if(i != ln1 and j != ln2):           
                if nums1[i] > nums2[j]:
                    x1 = nums2[j]
                    j += 1
                else:
                    x1 = nums1[i]
                    i += 1           
            elif(i < ln1):           
                x1 = nums1[i]
                i += 1
          
            # # if current index of nums1 is less than the length nums2
            else:           
                x1 = nums2[j]
                j += 1       
        return x1

    else:
        for count in range(((ln1 + ln2) // 2) + 1):        
            x2 = x1
            if(i != ln1 and j != ln2):       
                if nums1[i] > nums2[j]:
                    x1 = nums2[j]
                    j += 1
                else:
                    x1 = nums1[i]
                    i += 1           
            elif(i < ln1):           
                x1 = nums1[i]
                i += 1
             
            # if current index of nums2 is less than the length of it
            else:           
                x1 = nums2[j]
                j += 1    

        return (x1 + x2)/2
   
nums1 = [1,2]
nums2 = [3,4]

print(getSortedMedian(nums1, nums2))
