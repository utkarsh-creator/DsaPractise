class Solution:
    def romanToInt(self, s: str) -> int:
        mapi={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result=0
        for i in range(len(s)-1):
            if mapi[s[i]]<mapi[s[i+1]]:
                result -=mapi[s[i]]
            else:
                result +=mapi[s[i]]
        result +=mapi[s[-1]]
        return result
