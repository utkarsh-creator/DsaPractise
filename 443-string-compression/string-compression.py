from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0  
        n = len(chars)  
        
        i = 0  
        while i < n:
            char = chars[i]  
            count = 0  
            
            while i < n and chars[i] == char:
                count += 1
                i += 1
            
            chars[write_index] = char
            write_index += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit  
                    write_index += 1
        
        return write_index  

