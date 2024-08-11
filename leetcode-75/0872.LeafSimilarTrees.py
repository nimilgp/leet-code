class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafOrder(root, arr):
            if not root.left and not root.right:
                arr.append(root.val)
                return
            if root.left:
                leafOrder(root.left, arr)
            if root.right:
                leafOrder(root.right, arr)
        arr1 = []
        arr2 = []
        leafOrder(root1,arr1)
        leafOrder(root2, arr2)
        return arr1 == arr2
