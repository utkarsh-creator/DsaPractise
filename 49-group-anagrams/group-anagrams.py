class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            # Sort the word and use it as the key
            sorted_word = tuple(sorted(word))
            
            # If the key is not in the dictionary, add it with an empty list
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            
            # Append the original word to the list corresponding to the sorted key
            anagrams[sorted_word].append(word)
        
        # Return the list of all grouped anagrams
        return list(anagrams.values())
