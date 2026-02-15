# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        leftMost = root

        while leftMost.left:
            currNode = leftMost

            while currNode:
                currNode.left.next = currNode.right
                if currNode.next:
                    currNode.right.next = currNode.next.left
                currNode = currNode.next

            leftMost = leftMost.left

        return root