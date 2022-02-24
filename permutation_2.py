'''
Jhon Garcia
CS435 Recitation - 11/03/2021

Problem 2:

Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"

Output: true

Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"

Output: false
'''

from itertools import permutations

s1 = "ab"
s2 = "eidbaooo"

list_S1 = list(s1)
# Perms for s1
perm = permutations(list_S1)

# Temp array
tmp = []
for i in list(perm):
    tmp.append(''.join(i))

# Counter
test = 0
for i in tmp:
    if i in s2:
        # No Perm
        test = 1
        break

if(test == 0):
    print("False")
else:
    print("True")