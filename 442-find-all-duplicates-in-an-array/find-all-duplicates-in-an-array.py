class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        map_={}
        for num in nums:
            if num in map_:
                map_[num]+=1
            else:
                map_[num]=1
        duplicate=[]
        for num, count in map_.items():
            if count > 1:
                duplicate.append(num)
        
        return duplicate