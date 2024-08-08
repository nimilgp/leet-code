class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        val = 0
        def inorderTraversal(root):#L-N-R
            nonlocal count, val
            if not root:
                return 
            if root.left:
                inorderTraversal(root.left)
            count += 1
            if count == k:
                val = root.val
            if root.right:
                inorderTraversal(root.right)
        inorderTraversal(root)
        return val
