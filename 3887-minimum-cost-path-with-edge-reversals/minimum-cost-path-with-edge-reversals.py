import heapq

# constants equivalent to C++
N = 50000
USHRT_MAX = (1 << 16) - 1
UINT_MAX = (1 << 32) - 1

# adjacency list: each entry stores packed (weight, vertex)
adj = [[] for _ in range(N)]
dist = [UINT_MAX] * N


class Solution:
    @staticmethod
    def pack(w: int, v: int) -> int:
        # pack into uint64: high 48 bits = w, low 16 bits = v
        return (w << 16) | v

    @staticmethod
    def build_adj(n: int, edges):
        for i in range(n):
            adj[i].clear()

        for u, v, w in edges:
            adj[u].append(Solution.pack(w, v))       # normal edge
            adj[v].append(Solution.pack(2 * w, u))   # reversed edge

    @staticmethod
    def minCost(n: int, edges) -> int:
        Solution.build_adj(n, edges)

        # initialize distances
        for i in range(n):
            dist[i] = UINT_MAX

        pq = []
        dist[0] = 0
        heapq.heappush(pq, Solution.pack(0, 0))

        while pq:
            data = heapq.heappop(pq)
            d = data >> 16
            u = data & USHRT_MAX

            if d > dist[u]:
                continue
            if u == n - 1:
                return d

            for wv in adj[u]:
                w = wv >> 16
                v = wv & USHRT_MAX
                d2 = d + w

                if d2 < dist[v]:
                    dist[v] = d2
                    heapq.heappush(pq, Solution.pack(d2, v))

        return -1
