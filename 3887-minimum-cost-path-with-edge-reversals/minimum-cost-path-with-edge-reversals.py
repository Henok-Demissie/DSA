import heapq

USHRT_MASK = (1 << 16) - 1
UINT_MAX = (1 << 32) - 1


class Solution:
    def minCost(self, n, edges):
        adj = [[] for _ in range(n)]
        dist = [UINT_MAX] * n

        # build adjacency
        for u, v, w in edges:
            adj[u].append((w << 16) | v)
            adj[v].append(((w << 1) << 16) | u)

        hq = []
        dist0 = dist
        dist0[0] = 0
        heappush = heapq.heappush
        heappop = heapq.heappop

        heappush(hq, 0)  # pack(0, 0)

        while hq:
            data = heappop(hq)
            d = data >> 16
            u = data & USHRT_MASK

            if d != dist0[u]:
                continue
            if u == n - 1:
                return d

            for wv in adj[u]:
                nd = d + (wv >> 16)
                v = wv & USHRT_MASK
                if nd < dist0[v]:
                    dist0[v] = nd
                    heappush(hq, (nd << 16) | v)

        return -1
