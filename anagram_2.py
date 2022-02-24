'''
Jhon Garcia
CS435 Recitation - 10/27/2021

Problem 2:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

------------------------------------------------------------

Example 2:

Input: s = "rat", t = "car"

Output: false
'''

def areWordsAnagrams(s, t):
    # Function to check if words are Anagram
	l1 = len(s)
	l2 = len(t)

	# If the length of both is not the same can't be anagram
	if l1 != l2:
		return 0

	# Sort strings
	s = sorted(s)
	t = sorted(t)

	# Compare strings
	for i in range(0, l1):
		if s[i] != t[i]:
			return 0

	return 1

s = "rat"
t = "car"

if areWordsAnagrams(s, t):
	print("True")
else:
	print("False")

