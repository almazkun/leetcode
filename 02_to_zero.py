# Link https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        if 0 <= 0 <= 10**6:
            while num != 0:
                if num % 2 == 0:
                    num = num / 2
                    steps += 1 
                else:
                    num -= 1
                    steps += 1
            return steps
       
