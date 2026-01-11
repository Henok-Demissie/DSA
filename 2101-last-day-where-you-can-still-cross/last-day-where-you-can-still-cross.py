from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        top, bottom = n, n + 1

        parent = list(range(n + 2))
        rank = [0] * (n + 2)
        land = [False] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            a, b = find(a), find(b)
            if a == b:
                return
            if rank[a] < rank[b]:
                parent[a] = b
            elif rank[a] > rank[b]:
                parent[b] = a
            else:
                parent[b] = a
                rank[a] += 1

        for d in range(len(cells) - 1, -1, -1):
            r, c = cells[d][0] - 1, cells[d][1] - 1
            idx = r * col + c
            land[idx] = True

            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    nid = nr * col + nc
                    if land[nid]:
                        union(idx, nid)

            if r == 0:
                union(idx, top)
            if r == row - 1:
                union(idx, bottom)

            if find(top) == find(bottom):
                return d

        return 0