# MUST FIND SOLUTION USING hare and turtle
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        tmp = {}  
        for i in nums:
            if (i not in tmp):
                tmp[i] = 1
            else:
                return i
        return 0