class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for num in s:
            if num=="*":
                if stack:
                    stack.pop()
            else:
                stack.append(num)
        return ''.join(stack)