class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        
        for start in seen:
            if start - 1 not in seen:
                length = 1
                while length + start in seen:
                    length += 1    
                longest = max(longest, length)
                
        return longest