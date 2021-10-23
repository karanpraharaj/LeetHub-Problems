class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p1 = 0
        p2 = len(nums)-1
        sorted_sqrs = [0]*len(nums)
        p = len(nums)-1
        while(p1<=p2):
            if abs(nums[p1]) > abs(nums[p2]):
                sorted_sqrs[p] = nums[p1]**2
                p1 += 1
                
            else:
                sorted_sqrs[p] = nums[p2]**2
                p2 -=1
            p-=1    
        
        return sorted_sqrs