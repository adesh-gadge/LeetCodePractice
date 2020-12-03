# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode: 
        ans= self.cur = TreeNode(None)
        self.inorder(root)
        return ans.right
            
        
    def inorder(self,node):
        if node == None:
            return
        self.inorder(node.left)
        node.left  =None
        self.cur.right = node
        self.cur = node
        self.inorder(node.right)