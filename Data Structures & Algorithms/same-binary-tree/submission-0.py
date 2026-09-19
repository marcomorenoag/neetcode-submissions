# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Both empty/None -> are the same
        if not p and not q:
            return True
        # Just one may be empty/None -> are different
        if not p or not q:
            return False
        # Check current values and recursively the children's ones
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)