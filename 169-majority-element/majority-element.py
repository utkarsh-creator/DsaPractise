class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unmap={}
        majcount=len(nums)//2
        for num in nums:
            if num in unmap:
                unmap[num]+=1
            else:
                unmap[num]=1
            if unmap[num]>majcount:
                return num
