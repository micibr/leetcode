class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for gp in path.split('/'):
            if gp == '..':
                if stack:
                    stack.pop()
            elif not gp or gp == '.':
                continue
            else:
                stack.append(gp)

        return '/' + '/'.join(stack)

