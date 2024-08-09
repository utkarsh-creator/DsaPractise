class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        for words in strs:
            sorted_words=tuple(sorted(words))
            if sorted_words not in anagrams:
                anagrams[sorted_words]=[]
            anagrams[sorted_words].append(words)
        return list(anagrams.values())