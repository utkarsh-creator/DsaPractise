class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target_remainder = total_sum % p
        if target_remainder == 0:
            return 0
        prefix_sum = 0
        min_length = len(nums)
        remainder_map = {0: -1}
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            needed_remainder = (prefix_sum - target_remainder) % p
            if needed_remainder in remainder_map:
                min_length = min(min_length, i - remainder_map[needed_remainder])
            remainder_map[prefix_sum] = i
        return min_length if min_length < len(nums) else -1