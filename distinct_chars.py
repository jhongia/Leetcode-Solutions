'''
Jhon Garcia
CS435 Recitation - 09/29/2021

Given a string s, return the length of the longest substring that
contains at most two distinct characters.

Input: s = "eceba"

Output: 3

Explanation: The substring is "ece" which its length is 3.

Input: s = "ccaabbb"

Output: 5

Explanation: The substring is "aabbb" which its length is 5.
'''

s = "ccaabbb"
max_length = 0        
seen = {}

# Run as long as length of string is greater than 0
if(len(s) > 0):
    i = 0
    k = 0
    while k < len(s):
        char = s[k]
        
        if char in seen:
            seen[char] = seen[char] + 1
        else:
            seen[char] = 1
            
        if len(seen) > 2:   
            max_length = max(max_length, k - i)
            
            while len(seen) > 2:
                temp = s[i]
                count = seen[temp]
                if count > 1:
                    seen[temp] = count -1
                else:
                    del seen[temp]
                i += 1
        
        k += 1
        
    longest_substring = max(max_length, len(s) - i)
    print(longest_substring)

