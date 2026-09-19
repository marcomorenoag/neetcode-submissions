# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _dfs(self, node: TreeNode | None, depth: int) -> int:
        if not node:
            return depth
        # print(f'@_dfs: {node=} | {depth=}')
        return max(depth, self._dfs(node.left, depth+1), self._dfs(node.right, depth+1))
    
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        depth = self._dfs(root, 0)
        return depth