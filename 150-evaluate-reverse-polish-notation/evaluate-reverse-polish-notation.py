class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] not in ['+', '-', '*', '/']:
                stack.append(tokens[i])
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(num2 + num1)
                elif tokens[i] == '-':
                    stack.append(num2-num1)
                elif tokens[i] == '*':
                    stack.append(num2 * num1)
                else:
                    stack.append(int(num2 / num1))
            i += 1
        return int(stack.pop())