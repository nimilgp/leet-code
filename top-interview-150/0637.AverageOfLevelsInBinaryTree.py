class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque()
        if root:
            q.append(root)
        while(q):
            levelsum = 0
            lenq = len(q)
            for i in range(lenq):
                node = q.popleft()
                levelsum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(levelsum/lenq)
        return ans
