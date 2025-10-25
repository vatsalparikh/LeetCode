class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w
        distance = dict()
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            if node not in distance:
                distance[node] = time
                for end_node in graph[node]:
                    heapq.heappush(heap, (distance[node] + graph[node][end_node], end_node))
        if len(distance) == n:
            return max(distance.values())
        else:
            return -1