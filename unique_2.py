'''
Jhon Garcia
CS435 Recitation - 12/01/2021

Problem 2:

Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order. 

Example 1:

Input: nums = [1,1,2]

Output:[[1,1,2], [1,2,1], [2,1,1]]

Example 2:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
--------------------------------------------------------------------------------
'''

def permute_duplicates(nums):
    # Given a collection of numbers, nums, that might contain duplicates, 
    # return all possible unique permutations in any order.

    # Check for length
    if not nums or len(nums) == 1:
        return [nums]
    # Lists
    results, copied_list, temp = [], [], []
    # Iterate
    for num in nums:
        if not results:
            results = [[num]]
            continue
        for ar in results:
            assigned, seen = False, None
            for j in range(len(ar)+1):
                if seen == num and assigned:
                    continue
                t1 = ar[0:j] + [num] + ar[j:]
                if j < len(ar) and ar[j] == num:
                    assigned, seen = True, num
                # Append
                temp.append(t1)
            copied_list += temp
            temp = []
        results = copied_list
        copied_list = []

    return results
    
nums = [1,2,3]
print(permute_duplicates(nums))

