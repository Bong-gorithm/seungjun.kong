class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]

        oper = ['*', '/', '+', '-']
        oper_i = 0
        for i in range(n-1, 0, -1):
            if oper[oper_i] == '*':
                stack[-1] = stack[-1] * (i)
            elif oper[oper_i] == '/':
                stack[-1] = stack[-1] // (i)
            elif oper[oper_i] == '+':
                stack.append('+')
                stack.append(i)
            else:
                stack.append('-')
                stack.append(i)
            
            oper_i = (oper_i + 1) % 4

        output = stack[0]
        for i in range(1, len(stack)):
            if stack[i] == '+':
                output += stack[i+1]
            elif stack[i] == '-':
                output -= stack[i+1]
        return output