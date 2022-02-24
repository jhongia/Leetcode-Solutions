'''
Jhon Garcia
CS435 Recitation - 12/01/2021

Problem 3:

Given a string s that contains parentheses and letters, remove 
the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Input: s = "()())()"

Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"

Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("

Output: [""]
--------------------------------------------------------------------------------
'''

def remove_invalid_parentheses(s):
    # Given a string s that contains parentheses and letters, remove 
    # the minimum number of invalid parentheses to make the input string valid.
    results = []
    
    left, right = left_right(s)
    
    # Helper function
    rec(s, left, right, 0, results)
    
    return results
    
def left_right(s):
    # Check for left, right
    left = 0
    right = 0
    
    for parentheses in s:
        if parentheses == '(':
            left += 1
        elif parentheses == ')':
            if left > 0:
                left -= 1
            else:
                right += 1
                
    return left, right
    
def if_approved(s):
    left, right = left_right(s)
    return left == 0 and right == 0

def rec(s, left, right, start, results):
    if left == 0 and right == 0:
        if if_approved(s):
            results.append(s)
            return
    
    for i in range(start, len(s)):
        if i > start and s[i] == s[i - 1]:
            continue
            
        if s[i] == '(':
            rec(s[:i] + s[i + 1:], left - 1, right, i, results)
        elif s[i] == ')':
            rec(s[:i] + s[i + 1:], left, right - 1, i, results)


s = "(a)())()"
print(remove_invalid_parentheses(s))