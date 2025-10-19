class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        heaviest = 0
        while stones:
            heaviest = -heapq.heappop(stones)
            if stones:
                second_heaviest = -heapq.heappop(stones)
                if heaviest != second_heaviest:
                    heapq.heappush(stones, -(heaviest - second_heaviest))
                    print(stones)
                else:
                    heaviest = 0
        return heaviest
