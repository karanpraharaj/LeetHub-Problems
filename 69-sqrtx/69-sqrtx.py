class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return x
        
        sqrt = 0
        for i in range(1,int(x/2)+1):
            if i*i < x:
                sqrt = i
            
            elif i*i == x:
                return i
            
            elif i*i > x:
                break
        
        return sqrt