# https://leetcode.com/problems/fizz-buzz/
# https://leetcode.com/submissions/detail/600590490/
# Runtime: 44 ms (beats 89.09 % of python3 submissions)
# Memory Usage: 15.2 MB (beats 19.03 % of python3 submissions)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        theAnswer = []
        
        for i in range(n):
            counter = i + 1
            
            if counter % 3 == 0 and counter % 5 == 0:
                
                theAnswer.append("FizzBuzz")
                
            elif counter % 3 == 0:
                
                theAnswer.append("Fizz")
                
            elif counter % 5 == 0:
                
                theAnswer.append("Buzz")
                
            else:
                theAnswer.append(str(counter))
                
        return theAnswer