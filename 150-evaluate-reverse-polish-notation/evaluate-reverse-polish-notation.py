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
                    # ans = num2 / num1
                    stack.append(int(num2 / num1))
                    # if ans < 0:
                    #     stack.append('0')
                    # else:
                    #     stack.append(ans)
            i += 1
        return int(stack.pop())