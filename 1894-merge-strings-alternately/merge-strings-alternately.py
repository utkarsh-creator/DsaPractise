class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=len(word1)
        b=len(word2)
        result=[]
        count1=0
        count2=0
        while count1<a and count2<b:
            result.append(word1[count1])
            result.append(word2[count2])
            count1+=1
            count2+=1
        if count1<a:
            result.append(word1[count1:])
        if count2<b:
            result.append(word2[count2:]) 
        return ''.join(result)