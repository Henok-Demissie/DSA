class Solution(object):
    def largestTriangleArea(self, points):
        points = sorted(set(map(tuple, points)))
        if len(points) < 3:
            return 0.0

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        # -------- Convex Hull (Monotonic Chain) --------
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)

        hull = lower[:-1] + upper[:-1]
        m = len(hull)

        if m < 3:
            return 0.0

        # -------- Rotating Calipers (SAFE) --------
        max_area2 = 0

        for i in range(m):
            k = i + 2
            for j in range(i + 1, m - 1):
                if k <= j:
                    k = j + 1

                while k + 1 < m and abs(cross(hull[i], hull[j], hull[k + 1])) > abs(
                    cross(hull[i], hull[j], hull[k])
                ):
                    k += 1

                max_area2 = max(max_area2, abs(cross(hull[i], hull[j], hull[k])))

        return max_area2 / 2.0
