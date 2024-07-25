class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero=0
        count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[last_non_zero]=nums[i]
                last_non_zero +=1
            else:
                count+=1
        for j in range(last_non_zero,len(nums)):
            nums[j]=0
