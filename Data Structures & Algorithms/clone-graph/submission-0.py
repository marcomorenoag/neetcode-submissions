"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]
        ———
        BFS
        
        Time complexity: O(N) -> N is num of nodes
        Space complexity: O(N) -> N is num of nodes
        '''
        if not node:
            return
        
        visited = {} # k: original node -> v: cloned node
        queue = deque([node])
        visited[node] = Node(node.val)

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[cur].neighbors.append(visited[neighbor])
            
        return visited[node]