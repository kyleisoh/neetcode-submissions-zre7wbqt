class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_anagram = {}

        for word in strs:
            letters = [0] * 26
            
            for i in range(len(word)):
                idx = ord(word[i]) - ord('a')
                letters[idx] += 1

            if tuple(letters) not in seen_anagram:
                seen_anagram[tuple(letters)] = []
            seen_anagram[tuple(letters)].append(word)
        
        return seen_anagram.values()
