'''
Jhon Garcia
CS435 Recitation - 11/17/2021

Problem 2:

Given n pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.

Example 1:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1

Output: ["()"]
--------------------------------------------------------------------------------
'''

def addParentheses(n):
    # Functions generates all combinations of well-formed parentheses
    parentheses = []
    generator(n, n, '', parentheses)
    # When done return
    return parentheses

def generator(left, right, current, parentheses):
    if(left == 0):
        parentheses.append(current + ')' * right)
        return

    if(left < right):  # make sure have more '(' than ')'
        generator(left, right - 1, current + ')', parentheses)
    # Recursion
    generator(left - 1, right, current + '(', parentheses)

print(addParentheses(3))

