class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv }
        stack = list()
        for i in tokens:
            if i in operators:
                r = stack.pop()
                l = stack.pop()
                res = operators[i](l, r)
                stack.append(res)
            else:
                stack.append(int(i))
        return int(stack[-1])

