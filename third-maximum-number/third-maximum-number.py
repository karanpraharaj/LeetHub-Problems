class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = -inf
        second_max = -inf
        third_max = -inf
        
        for i in range(len(nums)):
            if nums[i] <first_max and nums[i]<second_max and nums[i] > third_max:
                third_max = nums[i]
            
            if nums[i] < first_max and nums[i] > second_max:
                second_max, third_max = nums[i], second_max
                
            if nums[i] > first_max:
                first_max, second_max, third_max = nums[i], first_max, second_max
                
            
        print(first_max, second_max, third_max)
        
        if third_max == -inf:
            third_max = first_max
        
        return third_max