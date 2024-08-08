class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:
                if stack:
                    top_element=stack.pop()
                else:
                    top_element="#"
                if bracket_map[char]!=top_element:
                    return False
            else:
                stack.append(char)
        return not stack
