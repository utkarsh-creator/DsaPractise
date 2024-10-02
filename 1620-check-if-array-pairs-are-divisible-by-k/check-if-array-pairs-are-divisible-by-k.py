from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Step 1: Calculate remainder frequencies
        remainder_count = Counter([x % k for x in arr])
        
        # Step 2: Check if pairs can be formed
        for remainder in remainder_count:
            if remainder == 0:
                # Count of elements with remainder 0 should be even
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                # Count of elements with remainder r should match remainder k-r
                if remainder_count[remainder] != remainder_count[k - remainder]:
                    return False
        
        return True
