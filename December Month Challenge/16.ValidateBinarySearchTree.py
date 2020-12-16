# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        l=[]
        self.traverse(root,l)
        prev = l[0]
        for i in range(1,len(l)):
            if l[i]<= prev:
                return False
            prev =l[i]
        return True
    
    def traverse(self,root,l):
        if root is None:
            return 
        self.traverse(root.left,l)
        l.append(root.val)
        self.traverse(root.right,l)
        
        
        