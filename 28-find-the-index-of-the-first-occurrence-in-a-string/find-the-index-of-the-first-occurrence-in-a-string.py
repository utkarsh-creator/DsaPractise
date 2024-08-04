class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is empty, return 0
        if not needle:
            return 0
        
        # Lengths of haystack and needle
        len_haystack = len(haystack)
        len_needle = len(needle)
        
        # If needle is longer than haystack, it can't be found
        if len_needle > len_haystack:
            return -1
        
        # Loop through haystack to find the needle
        for i in range(len_haystack - len_needle + 1):
            # Check if the substring of haystack starting at i matches needle
            if haystack[i:i + len_needle] == needle:
                return i
        
        # Needle was not found
        return -1
