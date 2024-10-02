class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sor=sorted(set(arr))
        hasmap={}
        rank=1
        for value in sor:
            hasmap[value]=rank
            rank+=1

        result=[]
        for num in arr:
            result.append(hasmap[num])
        return result
