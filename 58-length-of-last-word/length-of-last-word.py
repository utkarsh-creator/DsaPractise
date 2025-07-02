class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rev=s[::-1]
        a=rev.strip()
        count=0
        for i in range(0,len(a)):
            if a[i]!=" ":
                count+=1
            else:
                break
        return count