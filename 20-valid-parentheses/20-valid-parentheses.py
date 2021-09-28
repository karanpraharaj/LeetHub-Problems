class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(", "]":"[", "}":"{"}
        stack_open=[]
        stack_close=[]
        for i in range(len(s)-1,-1,-1):
            flag =True
            while stack_close and s[i]==dic[stack_close[-1]] and flag==True:
                stack_close.pop()
                flag=False   
            if s[i] in dic.keys():
                stack_close.append(s[i]) 
            elif s[i] in dic.values() and flag == True:
                return False
        return len(stack_close)==0 and len(stack_open)==0
        