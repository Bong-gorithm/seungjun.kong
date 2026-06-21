# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:
    def connect(self, root: Node) -> Node:

        if root is None:
            return None

        queue = deque([root])

        while queue:
            level_node_size = len(queue)
            prev = None

            for _ in range(level_node_size):
                node = queue.popleft()

                # 노드 연결
                if prev:
                    prev.next = node 
                
                # 이전 노드 기억하기
                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root