class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events=[]
        for num in intervals:
            start,end=num
            events.append((start,1))
            events.append((end+1,-1))
        events.sort()
        maxi=0
        active=0
        for i,j in events:
            active+=j
            maxi=max(maxi,active)
        return maxi