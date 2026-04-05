class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for number in nums:
            counter[number] = counter.get(number, 0) + 1

        for number, freq in counter.items():
            frequency[freq].append(number)
        
        output = []
        for i in range(len(frequency) - 1, 0, -1):
            if frequency[i]:
                output.extend(frequency[i])
        
        return output[0:k]
