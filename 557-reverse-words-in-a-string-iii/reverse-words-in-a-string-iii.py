class Solution:
    def reverseWords(self, s: str) -> str:
        arr=[]
        words=s.split()
        for num in words:
            arr.append(num[::-1])
        return ' '.join(arr)