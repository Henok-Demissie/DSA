class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dp(low, high):
            if low > high:
                return [None]
            res = []

            for i in range(low, high+1):
                for left in dp(low, i-1):
                    for right in dp(i+1, high):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

        return dp(1, n)