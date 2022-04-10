class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] < target:
                idx = i+1
            if nums[i] == target:
                return i
            
        return idx