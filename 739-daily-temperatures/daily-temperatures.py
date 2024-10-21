from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Initialize the answer list with zeros
        stack = []  # Stack to keep track of indices
        
        for i in range(n):
            # While stack is not empty and the current temperature is greater than
            # the temperature at the index stored at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()  # Pop the index from the stack
                answer[idx] = i - idx  # Calculate days until a warmer temperature
            stack.append(i)  # Push the current index onto the stack
        
        return answer
