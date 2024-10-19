class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # current_sum=0
        # k=len(nums)//2
        # for i in range(len(nums)):
            
        #     sum1=sum(nums[:k])
        #     sum2=sum(nums[k+1:])
        #     if sum1==sum2:
        #         return k
        #     else:
        #         if sum1>sum2:
        #             k-=1
        #         else:
        #             k+=1
        # return -1
        n = len(nums)
        
        for k in range(n):  # Iterate over all indices in the list
            sum1 = sum(nums[:k])    # Sum of elements before index k
            sum2 = sum(nums[k+1:])  # Sum of elements after index k
            
            if sum1 == sum2:  # If left sum equals right sum, return k as the pivot index
                return k
            
        return -1