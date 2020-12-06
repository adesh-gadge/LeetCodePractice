"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
The main idea is to go level by level and use already existing .next connections: if you will not do it, problem will be quite painful. So, idea is the following:

1) We will keep two nodes: node and curr: first one is for parent level and curr for next level.
(1.5) Dummy stores the beginning of the new level
2) We check if we have node.left and if we have, we create connection curr.next = node.left and also move our curr to the right, so it always will be the rightest visited node in level.
3) In similar way we check if we have node.right and do the same for it.
4) When we finished with node, we move it to right: node = node.next.
5) Finally, we need to go to the next level: we update node = dummy.next.
"""

class Solution:
    def connect(self, root):
        node = root
        while node:
            curr = dummy = Node(0)
            while node:  
                if node.left:
                    curr.next = node.left
                    curr = node.left
                if node.right:
                    curr.next = node.right
                    curr = curr.next 
                node = node.next
            node = dummy.next
            
               
        return root