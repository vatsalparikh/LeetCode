# 1, 2, 3, 4 -> 2, 2, 6, 4

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        min_val = float('inf')
        deviation = float('inf')

        for n in nums:
            if n % 2:
                n *= 2
            heapq.heappush(heap, -n)
            min_val = min(min_val, n)

        while True:
            max_val = -heapq.heappop(heap)
            deviation = min(deviation, max_val - min_val)

            if max_val % 2:
                break

            new_val = max_val // 2
            min_val = min(min_val, new_val)
            heapq.heappush(heap, -new_val)

        return deviation