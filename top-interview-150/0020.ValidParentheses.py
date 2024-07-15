class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(","{", "["]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                match char:
                    case ")":
                        if top != "(":
                            return False
                    case "}":
                        if top != "{":
                            return False
                    case "]":
                        if top != "[":
                            return False
        if len(stack) == 0:
            return True
        else:
            return False
