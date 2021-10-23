class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(set(nums))
        disappeared = []
        for i in range(1, len(nums)+1):
            if i not in counter:
                disappeared.append(i)
                
        return disappeared