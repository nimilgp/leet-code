class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev, mindiff = float("inf"), float("inf")
        def inorderTraversal(root):#L-N-R
            nonlocal prev, mindiff
            if not root:
                return
            if root.left:
                inorderTraversal(root.left)
            if abs((root.val - prev)) < mindiff:
                mindiff = abs(root.val - prev)
            prev = root.val
            if root.right:
                inorderTraversal(root.right)
        inorderTraversal(root)
        return mindiff
