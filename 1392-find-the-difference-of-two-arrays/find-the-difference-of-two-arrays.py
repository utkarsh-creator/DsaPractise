class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=set(nums1)
        set2=set(nums2)
        a=list(set1-set2)
        b=list(set2-set1)
        return [a,b]