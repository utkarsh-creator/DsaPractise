class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack=[]
        result=0
        for num in arr:
            while stack and stack[-1]<=num:
                mid=stack.pop()
                if stack:
                    result += mid*min(stack[-1],num)
                else:
                    result +=mid*num
            stack.append(num)
        while len(stack)>1:
            result+=stack.pop() * stack[-1]
        return result