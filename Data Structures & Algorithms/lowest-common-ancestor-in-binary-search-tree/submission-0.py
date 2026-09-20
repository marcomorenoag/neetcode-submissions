# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _binary_search(self, node: TreeNode, target: TreeNode, path: List[TreeNode]) -> List[TreeNode]:
        # print(f'{node=}')
        if not node:
            return None
        path.append(node)
        if target.val == node.val:
            return path
        if target.val < node.val:
            return self._binary_search(node.left, target, path)
        return self._binary_search(node.right, target, path)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
                 Stack
        BS(2) -> [6,2]
        BS(8) -> [6,8]
        ---
        BS(2) -> [6,2]
        BS(4) -> [6,2,4]
        ---
        1. BS of p and q
        2. Track their finding paths – stacks
        3. For the longest stack, pop elements and stop until the first one that exists for the other stack -> findingthe LCA
        '''
        # 1 & 2
        p_node = self._binary_search(root, p, [])
        q_node = self._binary_search(root, q, [])
        # print(f'{p_node=} | {q_node=}')

        # 3
        longest_path = p_node
        shortest_path = q_node
        if len(q_node) > len(p_node):
            longest_path = q_node
            shortest_path = p_node
        while len(longest_path):
            backtracked_node = longest_path.pop(-1)
            if backtracked_node in shortest_path:
                return backtracked_node
        return root
