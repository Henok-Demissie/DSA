# Python implementation
class Solution:
    def buildTree(self, preorder, inorder):
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.index = 0

        def helper(start, end):
            if start > end:
                return None
            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)

            mid = idx_map[root_val]
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root

        return helper(0, len(inorder) - 1)