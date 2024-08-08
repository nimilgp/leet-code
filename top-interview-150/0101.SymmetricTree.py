class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None or root1.val != root2.val:
                return False
            return isSame(root1.left, root2.right) and isSame(root1.right, root2.left)
        if not root:
            return True
        return isSame(root.left, root.right)
