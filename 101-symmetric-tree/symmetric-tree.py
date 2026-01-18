class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        def check(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return check(p.left, q.right) and check(p.right, q.left)

        return check(root.left, root.right)