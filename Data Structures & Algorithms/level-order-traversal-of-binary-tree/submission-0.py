# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        '''
        - BFS -> queue
        - Hash Map: k (level) -> val (list of nodes' values)
        '''
        if not root:
            return []
        
        queue = deque([(root, 1)]) # (val,level)
        level_to_nodes_map: dict[int, List[int]] = defaultdict(list)
        while len(queue):
            node, level = queue.popleft()
            if not node:
                continue
            level_to_nodes_map[level].append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        response = []
        for item in level_to_nodes_map:
            response.append(level_to_nodes_map[item])
        return response