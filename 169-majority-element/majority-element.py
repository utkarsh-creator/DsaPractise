class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

            



        # unmap={}
        # majcount=len(nums)//2
        # for num in nums:
        #     if num in unmap:
        #         unmap[num]+=1
        #     else:
        #         unmap[num]=1
        #     if unmap[num]>majcount:
        #         return num
