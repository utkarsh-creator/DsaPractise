class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        result=0
        a=list(s)
        for i in range(len(a)):
            if a[i]=='(':
                count+=1
            else:
                if count>0:
                    count-=1
                else:
                    result+=1
        return count+result