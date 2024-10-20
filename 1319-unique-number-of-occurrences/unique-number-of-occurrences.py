class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mapi={}

        for num in arr:
            if num not in mapi:
                mapi[num]=1
            else:
                mapi[num]+=1
        
        occurence=set(mapi.values())
        return len(occurence)==len(mapi)
        # count=0
        # for i,num in enumerate(mapi):
        #     if num>0:
        #         count+=1
        #     else:
        #         count-=1
        # n=len(arr)
        # if n==count:
        #     return False
        # else:
        #     return True