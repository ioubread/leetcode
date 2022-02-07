# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
# https://leetcode.com/submissions/detail/636401248/
# Runtime: 79 ms (beats 57.00% of python3 submissions)
# Memory Usage: 14.2 MB (beats 80.63% of python3 submissions)

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        finalchanceused = False
        previousnumber = None
        twonumbersback = None
        
        
        for num in nums:
            print(finalchanceused)
            
            if previousnumber == None:
                previousnumber = num
                continue
            
            else:
                
                if num > previousnumber:
                    twonumbersback = previousnumber
                    previousnumber = num
                    continue
                
                else:
                    if twonumbersback == None:
                        
                        if finalchanceused == True:
                            return False
                        
                        else:
                            finalchanceused = True
                            previousnumber = num
                            continue

                    else:
                        
                        if finalchanceused == True:
                            return False

                        if num > twonumbersback:
                            finalchanceused = True
                            previousnumber = num
                            continue

                        else:

                            if finalchanceused == True:
                                return False

                            else:

                                finalchanceused = True
                                continue

        return True
