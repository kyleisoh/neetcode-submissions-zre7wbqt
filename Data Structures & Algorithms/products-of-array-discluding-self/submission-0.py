class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        previous = 1
        idx = 0
        
        for i in range(len(nums)):
            multiple = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                multiple *= nums[j]
            output.append(multiple)
                    
        return output
            
            