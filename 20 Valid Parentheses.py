# https://leetcode.com/problems/valid-parentheses/
# Runtime: 32 ms (beats 88.50 % of python3 submission)
# Memory Usage: 14.3 MB


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        validBrackets = ["[]", "()", "{}"]
        
        
        for c in s:
            if c == "("  or c == "[" or c == "{":
                stack.append(c)
            else: # closing
                if len(stack) > 0:
                    # r = stack.pop()
                    # r = [ { (
                    myStr = stack[-1] + c
                    
                    if myStr in validBrackets:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
        return len(stack) == 0