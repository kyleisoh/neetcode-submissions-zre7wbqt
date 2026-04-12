class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        longest = 0

        for number in uniqueNums:
            if number - 1 not in uniqueNums:
                length = 1
                while number + length in uniqueNums:
                    length += 1
                longest = max(longest, length)

        return longest