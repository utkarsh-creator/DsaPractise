class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        maxi=0
        for num in prices:
            mini=min(mini,num)
            maxi=max(maxi,(num-mini))
        return(maxi)
            