'''
Jhon Garcia
CS435 Recitation - 10/20/2021

Problem 3: 

Given a string s and an integer k, return the length of the longest 
substring of s that contains at most k distinct characters.

Input: s = "eceba", k = 2

Output: 3

The substring is "ece" with length 3.

Input: s = "aa", k = 1

Output: 2

The substring is "aa" with length 2. 
'''

def lengthOfLongestSubstring(s, k):
        if k == 0:
            return 0
        
        n = len(s)
        disc = {}
        long = j = 0
        for i in range(n):
            while j < n:
                # update index of last seen
                disc[s[j]] = j 
                if len(disc) <= k:
                    long = max(long, j + 1 - i) 
                else:
                    break 
                j += 1

            if disc[s[i]] == i: 
                # remove if last one seen
                del disc[s[i]]
        return long

s = "aa"
k = 1

print(lengthOfLongestSubstring(s, k))