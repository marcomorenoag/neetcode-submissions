# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _dfs(self, node: TreeNode | None, lower: int, upper: int) -> bool:
        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False 

        return self._dfs(node.left, lower, node.val) and self._dfs(node.right, node.val, upper)
    
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self._dfs(root, float('-inf'), float('inf'))