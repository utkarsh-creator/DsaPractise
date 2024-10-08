class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyType.sort()
        count=1
        for i in range(len(candyType)-1):
            if (candyType[i]!=candyType[i+1]):
                count+=1
        
        n=len(candyType)
        ans=n//2
        return min(count,ans)