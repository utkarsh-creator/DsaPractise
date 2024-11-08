class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapi={}
        
        for num in s:
            if num not in mapi:
                mapi[num]=1
            else:
                mapi[num]+=1
        for i,j in enumerate(s):
            if mapi[j]==1:
                return i
        return -1