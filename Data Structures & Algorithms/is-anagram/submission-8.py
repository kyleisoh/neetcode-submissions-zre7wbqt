class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ordinance = [0] * 26
        ordinance2 = [0] * 26

        for i in range(0, len(s)):
            ordinance[ord(s[i]) - ord('a')] += 1
        
        for j in range(0, len(t)):
            ordinance2[ord(t[j]) - ord('a')] += 1
        
        return ordinance == ordinance2