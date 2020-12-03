# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode: 
        l=[]
        self.inorder(root,l)
        t = TreeNode(val=l[0])
        head = t
        for i in l[1:]:
            t.right = TreeNode(val=i)
            t = t.right
        return head
            
    #in order traversal for asc ordered list
    def inorder(self,head,l):
        if head == None:
            return
        self.inorder(head.left,l)
        l.append(head.val)
        self.inorder(head.right,l)