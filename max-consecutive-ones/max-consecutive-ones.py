class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        ct = 0
        for i in nums:
            
            if i == 1:
                ct += 1
            else:
                ct = 0
            max = ct if ct>max else max
        
        return max