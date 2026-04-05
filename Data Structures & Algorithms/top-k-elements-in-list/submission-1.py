class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        output = []

        for number in nums:
            counter[number] = counter.get(number, 0) + 1

        for number, freq in counter.items():
            output.append((number, freq))
        
        output.sort(reverse=True, key=lambda x:x[1])

        return [output[i][0] for i in range(k)]
