class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, left, right):#L-N-R
            if not root:
                return True
            if not(left < root.val < right):
                return False
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)
        return valid(root, float("-inf"),float("inf"))
