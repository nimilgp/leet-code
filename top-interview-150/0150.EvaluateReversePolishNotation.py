class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for c in tokens:
            if c in operators:
                val1 = stack.pop()
                val2 = stack.pop()
                val = 0
                match c:
                    case "+":
                        stack.append(val2 + val1)
                    case "-":
                        stack.append(val2 - val1)
                    case "*":
                        stack.append(val2 * val1)
                    case "/":
                        stack.append(int(val2 / val1))
            else:
                stack.append(int(c))
        return stack[0]
