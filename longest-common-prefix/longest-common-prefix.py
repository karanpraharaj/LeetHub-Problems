class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        min_str = min(strs, key=len)
        
        lcp = min_str
        lcp_pair = ""
    
        for word in strs:
            lcp_pair = ""
            for i in range(len(min_str)):
                if word[i] == min_str[i]:
                    lcp_pair = lcp_pair + word[i]
                    
                else:
                    lcp = lcp_pair if len(lcp_pair)<len(lcp) else lcp
           
        return lcp
            
        
    