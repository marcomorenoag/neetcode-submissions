# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Tuple, Optional
from collections import deque

class Solution:
    def _dfs_in_order(self, node: TreeNode | None, nodes: []) -> List[int]:
        if not node:
            return nodes

        self._dfs_in_order(node.left, nodes)
        nodes.append(node.val)
        self._dfs_in_order(node.right, nodes)
        return nodes

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        '''
        APPROACH
        1. Traverse the tree in DFS In-Order
        2. Store each value visited into a list
        3. Return the list and return the k - 1
        ---
        ANALYSIS
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        values = self._dfs_in_order(root, [])
        return values[k - 1]