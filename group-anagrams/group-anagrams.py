class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for i in range(len(strs)):
            charcount = [0]*26
            for c in strs[i]:
                charcount[ord(c)-ord('a')] +=1
            
            if tuple(charcount) not in anagrams:
                anagrams[tuple(charcount)] = [strs[i]]
            
            else:
                anagrams[tuple(charcount)].append(strs[i])
        
        return (anagrams.values())