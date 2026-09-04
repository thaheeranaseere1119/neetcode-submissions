# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if t is None:
            return True
        if s is None:
            return False
        if self.same(s,t):
            return True
        return(self.isSubtree(s.left, t)or self.isSubtree(s.right,t) )
    def same(self,s,t):
        if s is None and t is None:
            return True
        if s is None or t is None or s.val!=t.val:
            return False
        return ((self.same(s.left, t.left)and self.same(s.right,t.right)))

        