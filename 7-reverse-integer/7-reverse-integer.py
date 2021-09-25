class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        x1 = x
        flag = 0
        if x1 < 0:
            x1 = 0-x1
            flag = 1
            
        while x1>0:
            r = x1%10
            print(r)
            x1 = int(x1/10)
            print(x1)
            sum = (sum*10)+r
            print(sum)
        
        if flag == 1:
            sum = 0-sum
        
        if sum > 2**31 or sum < -2**31:
            return 0
        
        return sum