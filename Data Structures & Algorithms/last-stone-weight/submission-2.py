class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_num = [-1 * num for num in stones]
        heapq.heapify(neg_num)

        while len(neg_num) > 1:
            first, second = heapq.heappop(neg_num) * -1, heapq.heappop(neg_num) * -1
            if first == second:
                continue
            if first > second:
                heapq.heappush(neg_num, (first - second) * -1)
        
        if not neg_num:
            return 0
        return neg_num[0] * -1

            