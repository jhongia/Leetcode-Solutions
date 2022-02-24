'''
Jhon Garcia
CS435 Recitation - 10/27/2021

Problem 1:

Given two strings s and t, return true if they are both one edit 
distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

Example 1:

Input: s = "ab", t = "acb"

Output: true

Explanation: We can insert 'c' into s to get t.

------------------------------------------------------------

Example 2:

Input: s = "", t = ""

Output: false

Explanation: We cannot get t from s by only one step.

------------------------------------------------------------

Example 3:

Input: s = "", t = "A"

Output: true

Problem generalization : Edit distance

Given two words word1 and word2, find the minimum number of operations 
required to convert word1 to word2. The naive approach would be to check 
for all possible edit sequences and choose the shortest one in-between. 
That would result in an exponential complexity and it's an overkill since 
we actually don't need to have all possible edit sequences but just the 
shortest one.
'''

def edit_distance(s, t):
    # Function to check two strings s and t, are both one edit distance apart

	# Find lengths of given strings
	ls = len(s)
	ln = len(t)

	# If the lengths difference between lengths is greater than 1 then return False
	if abs(ls - ln) > 1:
		return False

	# Counter for edit distance
	count = 0

	# Helper counters
	i = 0
	j = 0

	while i < ls and j < ln:
		# If characters do not match
		if s[i] != t[j]:
			if count == 1:
				return False

			# If one length is greater, then remove a character
			if ls > ln:
				i += 1
			elif ls < ln:
				j += 1
				
			# If the lengths of both strings are the same
			else: 
				i += 1
				j += 1

			# Add 1 to the edit distance counter
			count += 1

		# If the characters do not match
		else: 
			i += 1
			j += 1

	# If there are any extra characters in strings
	if i < ls or j < ln:
		count += 1

	return count == 1

s = ""
t = "A"

if edit_distance(s, t):
	print("True")
else:
	print("False")

