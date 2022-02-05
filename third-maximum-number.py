# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        firstNumber = None
        secondNumber = None
        thirdNumber = None
        
        for num in nums:
            
            if secondNumber == None:
                secondNumber = num
            
            elif secondNumber == num:
                continue
            
            elif num > secondNumber:
                
                if thirdNumber == None:
                    thirdNumber = num
                
                elif thirdNumber == num:
                    continue
                
                elif num > thirdNumber:
                    firstNumber = secondNumber
                    secondNumber = thirdNumber
                    thirdNumber = num
                
                elif num < thirdNumber:
                    firstNumber = secondNumber
                    secondNumber = num
                    
            elif num < secondNumber:
                if firstNumber == None:
                    firstNumber = num
                
                elif firstNumber == num:
                    continue
                
                elif num > firstNumber:
                    firstNumber = num
                
                elif num < firstNumber and thirdNumber == None:
                    thirdNumber = secondNumber
                    secondNumber = firstNumber
                    firstNumber = num
                    
        if (not firstNumber == None) and (not thirdNumber == None):
            return firstNumber
        
        else:
            if (not thirdNumber == None):
                return thirdNumber
            else:
                return secondNumber
