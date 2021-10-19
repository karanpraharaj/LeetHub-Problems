class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ct = 0
        if nums != []:
            unique = nums[0]
            dup = 0
            nums[ct] = unique
            ct+=1
            for i in range(len(nums)):
                if nums[i] == unique:
                    pass
                else:
                    unique = nums[i]
                    nums[ct] = unique
                    ct+=1

            del nums[ct:]
