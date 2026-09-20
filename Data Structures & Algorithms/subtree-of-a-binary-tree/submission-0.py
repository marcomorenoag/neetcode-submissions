# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _dfs(self, node: TreeNode | Node, sub_tree: TreeNode | None) -> bool:
        if not node:
            return False

        if self._is_same_tree(node, sub_tree):
            return True

        return self._dfs(node.left, sub_tree) or self._dfs(node.right, sub_tree)

    def _is_same_tree(self, sub_tree_one: TreeNode | None, sub_tree_two: TreeNode | None) -> bool:
        if not sub_tree_one and not sub_tree_two:
            return True
        if not sub_tree_one or not sub_tree_two:
            return False
        return sub_tree_one.val == sub_tree_two.val and self._is_same_tree(sub_tree_one.left, sub_tree_two.left) and self._is_same_tree(sub_tree_one.right, sub_tree_two.right)
        

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        return self._dfs(root, subRoot)