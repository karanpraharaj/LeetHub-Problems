class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc_start = 0
        dec_start = 0
        state = ""
        for i in range(1, len(arr)):
            if arr[i]>arr[i-1]:
                if state=="-":
                    return False
                if state=="":
                    inc_start+=1
                
                state = "+"
                
            elif arr[i]<arr[i-1]:
                if state == "+":
                    dec_start+=1
                
                state = "-"
            
            elif arr[i] == arr[i-1]:
                return False
        
        if inc_start == 1 and dec_start == 1:
            return True
        
        else:
            return False