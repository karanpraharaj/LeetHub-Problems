class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def get_prefix(str_a, str_b):
            prefix = ""
            length = min(len(str_a), len(str_b))
            i = 0
            while i < length and (str_a[i] == str_b[i]):
                prefix += str_a[i]
                i += 1
                
            return prefix
        
        return reduce(get_prefix, strs)
        