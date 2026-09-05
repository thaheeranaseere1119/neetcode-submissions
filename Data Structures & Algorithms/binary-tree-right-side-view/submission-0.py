from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        c = deque([root])
        while c:
            rightside = None
            for i in range(len(c)):
                node = c.popleft()
                if node:
                    rightside = node
                    c.append(node.left)
                    c.append(node.right)
            if rightside:
                res.append(rightside.val)
        return res