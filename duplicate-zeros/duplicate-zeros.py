class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        orig_len = len(arr)
        i = 0
        print(orig_len)
        while(i<orig_len):
            if arr[i] == 0:
                arr.insert(i,0)
                i+=2
                
            else:
                i+=1
            
            if i>orig_len:
                break
        print(len(arr))
        print(arr[orig_len:len(arr)])
        if len(arr)>orig_len:
            del arr[orig_len:len(arr)]