class BFSSolution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        queue = deque([(src, 0, 0)])
        min_cost = [float('inf')] * n
        min_cost[src] = 0

        while queue:
            city, cost, stops = queue.popleft()

            if stops <= k:
                for neighbor, price in graph[city].items():
                    new_cost = cost + price
                    if new_cost < min_cost[neighbor]:
                        min_cost[neighbor] = new_cost
                        queue.append((neighbor, new_cost, stops + 1))

        if min_cost[dst] != float('inf'):
            return min_cost[dst]
        else:
            return -1

class BellmanFordSolution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k+1):
            temp = prices.copy()
            for u, v, w in flights: # u is source, v is destination, w is price
                if prices[u] == float('inf'):
                    continue
                temp[v] = min(temp[v], prices[u] + w)
            prices = temp
        
        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]

'''
4 -> 1
1 -> 2
0 -> 3
0 -> 4
3 -> 1
1 -> 4
'''