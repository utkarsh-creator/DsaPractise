class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current_count = 0
        max_count = 0
        
        # Step 1: Count vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_count = current_count
        
        # Step 2: Slide the window over the rest of the string
        for i in range(k, len(s)):
            # Remove the leftmost character of the previous window
            if s[i - k] in vowels:
                current_count -= 1
            # Add the rightmost character of the current window
            if s[i] in vowels:
                current_count += 1
            
            # Update max_count if the current window has more vowels
            max_count = max(max_count, current_count)
        
        return max_count
