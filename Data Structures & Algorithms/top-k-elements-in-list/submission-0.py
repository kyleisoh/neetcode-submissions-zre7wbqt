class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for number in nums:
            if number not in seen:
                seen[number] = 0
            seen[number] += 1
        
        freq_lst = []
        for key, value in seen.items():
            freq_lst.append((key, value))
    
        sorted_lst = sorted(freq_lst, reverse=True, key=lambda x: x[1])

        output = []
        for i in range(k):
            output.append(sorted_lst[i][0])
        
        return output
            
