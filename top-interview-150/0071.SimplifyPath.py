class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/')
        for d in directories:
            if d == '.' or not d:
                continue
            elif d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return '/' + '/'.join(stack)
