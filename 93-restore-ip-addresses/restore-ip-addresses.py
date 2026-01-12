class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(index, path):
            # BASE CASE:
            # If we have 4 parts AND used all characters
            if len(path) == 4:
                if index == len(s):
                    res.append(".".join(path))
                return

            # Try taking 1 to 3 digits
            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                # Rule 1: No leading zero
                if part[0] == '0' and len(part) > 1:
                    continue

                # Rule 2: Value <= 255
                if int(part) > 255:
                    continue

                # Choose
                path.append(part)

                # Explore
                backtrack(index + length, path)

                # Un-choose (BACKTRACK)
                path.pop()

        backtrack(0, [])
        return res
        