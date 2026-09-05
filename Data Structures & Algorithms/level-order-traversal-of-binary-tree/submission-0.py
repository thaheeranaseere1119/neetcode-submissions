# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        c=deque()
        c.append(root)
        res=[]
        while c:
            level=[]
            for i in range(len(c)):
                node=c.popleft()
                if node:
                    level.append(node.val)
                    c.append(node.left)
                    c.append(node.right)
            if level:
                res.append(level)
        return res


            

        