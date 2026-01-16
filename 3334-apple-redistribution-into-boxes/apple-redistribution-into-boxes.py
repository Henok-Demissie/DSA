class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Calculate total apples
        total = sum(apple)
        # Sort in descending order to pick largest boxes first
        capacity.sort(reverse=True)
        
        cnt = 0
        for cap in capacity:
            total -= cap
            cnt += 1
            if total <= 0:
                return cnt
        return cnt