class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxLevel = 1
        maxSum = float("-inf")
        level = 1
        q = [root]
        while q:
            s = 0
            for i in range(len(q)):
                node = q.pop(0)
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > maxSum:
                maxSum = s
                maxLevel = level
            level += 1
        return maxLevel
