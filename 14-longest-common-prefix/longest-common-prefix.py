class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i>=len(s) or s[i]!=strs[0][i]:
                    return strs[0][:i]
        return strs[0]
 
 
 
 
        # if not strs:
        #     return ""
        # prefix=strs[0]
        # for string in strs[1:]:
        #     while string.find(prefix)!=0:
        #         prefix=prefix[:-1]
        #         if not prefix:
        #             return ""
        # return prefix
