class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for i in range(len(s)):
            if s[i].isalnum():
                stack1.append(s[i])
            elif s[i]=="#":
                if stack1:
                    stack1.pop()
        for i in range(len(t)):
            if t[i].isalnum():
                stack2.append(t[i])
            elif t[i]=="#":
                if stack2:
                    stack2.pop()
        return stack1==stack2
                
        
        


        