class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i, integer in enumerate(nums):
            if integer in seen:
                return True
            seen[integer] = i
        
        return False