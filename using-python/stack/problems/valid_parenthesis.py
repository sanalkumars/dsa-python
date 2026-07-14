# problem statement 

# 1. Balanced Parentheses / Valid Brackets
# Problem Statement:
# Given a string s containing just the characters (, ), {, }, [, and ], determine if the input string is valid.
# An input string is valid if:

# Open brackets must be closed by the same type of bracket.
# Open brackets must be closed in the correct order.
# Every closing bracket has a corresponding open bracket of the same type.

# optimised solution

def isValid(s):
    stack = []
    map={
        ")" : "(",
        "]" :"[",
        "}" : "{"
    }

    for c in s :
        if c in "({[":  # means if the character is a open one we simply push it in to the stack 
            stack.append(c)
        else:
            if not stack: return False
            if map[c] == stack[-1]:
                stack.pop()
            else: 
                return False
    if len(stack) > 0 : return False
    else:
        return True

    


            
    
