class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Initialize a hash map to store the count of remainders when prefix sums are divided by k
        remainder_count = {0: 1}  # Start with remainder 0 having one occurrence
        prefix_sum = 0  # To store the running sum of elements
        count = 0  # To store the number of valid subarrays

        # Iterate through each number in the list
        for num in nums:
            prefix_sum += num  # Update the prefix sum with the current number
            remainder = prefix_sum % k  # Calculate the remainder of the prefix sum divided by k
            
            # Adjust for negative remainders to ensure non-negative values
            if remainder < 0:
                remainder += k
            
            # If this remainder has been seen before, it means there are subarrays with sums divisible by k
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            # Update the hash map with the current remainder
            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1
        
        return count  # Return the total count of valid subarrays
