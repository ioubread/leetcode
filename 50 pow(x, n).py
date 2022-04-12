# https://leetcode.com/problems/powx-n/
# https://leetcode.com/submissions/detail/600649371/
# Runtime: 16 ms (beats 90.94 % of python submissions)
# Memory Usage: 13.2 MB (beats 89.60 % of python submissions)


class Solution(object):
    def myPow(self, x, n):
        
        if n < 0:
            n = abs(n)
            wasNegative = True
            
        else:
            wasNegative = False

        if n == 0:
            
            return 1
        
        elif n == 1:
            
            if wasNegative:
                x = 1/x
            
            return x
        
        elif not (n % 2 == 0):

            compute = self.myPow(x, n / 2)
            
            result = x * compute * compute
            
            if wasNegative:
                result = 1 / result
            
            return result
            
        else:
            
            compute = self.myPow(x, n / 2)
            
            result = compute * compute
            
            if wasNegative:
                result = 1 / result
            
            return result