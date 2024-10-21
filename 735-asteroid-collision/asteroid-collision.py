class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for num in asteroids:
            while stack and num<0 and stack[-1]>0:
                if abs(num)>stack[-1]:
                    stack.pop()
                    continue
                elif abs(num)==stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(num)
        return stack
            