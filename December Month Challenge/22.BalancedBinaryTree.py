# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root):
        if root is None:
            return 0
        
        lHt = self.height(root.left)         
        rHt = self.height(root.right)
    
        if lHt > rHt:
            return lHt +1
        else:
            return rHt +1
        
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        lH = self.height(root.left)
        rH = self.height(root.right)
        if abs(lH - rH) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
             return False
    
