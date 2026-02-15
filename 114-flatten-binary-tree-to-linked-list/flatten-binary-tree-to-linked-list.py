# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            if curr.left:
                # 1. Find the 'tail' of the left subtree
                # (The rightmost node in the left subtree)
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # 2. HEURISTIC: Graft the current right subtree 
                # onto the end of the left subtree's tail.
                predecessor.right = curr.right
                
                # 3. Move the modified left subtree to the right
                curr.right = curr.left
                curr.left = None
            
            # 4. Move to the next node in our growing 'Vine'
            curr = curr.right