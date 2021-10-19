class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        p1 = 0
        p2 = len(nums)-1
        insert = len(nums)-1
        
        while(p1<=p2):
            if abs(nums[p1]) >= abs(nums[p2]):
                res[insert] = nums[p1]*nums[p1]
                p1 = p1+1
                
            else:
                res[insert] = nums[p2]*nums[p2]
                p2 = p2-1
            
            insert -= 1
    
        return res