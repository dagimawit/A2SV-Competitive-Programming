class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ['+', '-', '*', '/']
        stack = []

        for char in tokens:
            if char not in operator:
                stack.append(int(char))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    result = num1 + num2
                elif char == '-':
                    result = num1 - num2
                elif char == '*':
                    result = num1 * num2
                elif char == '/':
                    result = int(num1 / num2)
                stack.append(result)

        return stack.pop()