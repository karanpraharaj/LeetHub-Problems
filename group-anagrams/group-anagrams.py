class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return None
        
        anagrams = defaultdict(list)
        
        for i in strs:
            anchor = ''.join(sorted(i))
            anagrams[anchor].append(i)
        
        return anagrams.values()