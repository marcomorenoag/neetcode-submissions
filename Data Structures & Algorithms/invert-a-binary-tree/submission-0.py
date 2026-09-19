# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _invert_node(self, node: TreeNode | None) -> None:
        if node is None:
            return

        left = node.left
        node.left = node.right
        node.right = left
        # print(f'@ _invert_node : {node}')
        self._invert_node(node.left)
        self._invert_node(node.right)
        return
    
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return
        
        self._invert_node(root)
        # print(f'{root=}')
        return root