class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        count=0
        for word in words:
            if set(word).issubset(a):
                count+=1
        return count