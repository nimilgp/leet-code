class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        if root:
            q.append(root)
        while q:
            level = deque()
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node)
            while (len(level) > 1):
                node = level.popleft()
                node.next = level[0]
        return root
