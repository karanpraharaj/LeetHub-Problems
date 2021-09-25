class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev_s = str(x)[::-1]
        if s == rev_s:
            return True
        
        return False