class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters, t_letters = {}, {}
        
        for letter in s:
            if letter not in s_letters:
                s_letters[letter] = 1
            else:
                s_letters[letter] += 1
        
        for letter in t:
            if letter not in t_letters:
                t_letters[letter] = 1
            else:
                t_letters[letter] += 1
        
        return s_letters == t_letters
