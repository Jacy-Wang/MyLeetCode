class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in xrange(len(tokens)):
            if tokens[i].isdigit() or (len(tokens[i]) >= 2 and tokens[i].startswith('-')):
                stack.append(tokens[i])
            else:
                second = stack.pop()
                first = stack.pop()
                if tokens[i] == '/':
                    stack.append(str(int(float(first) / int(second))))
                else:
                    stack.append(str(eval(first + tokens[i] + second)))
        return int(stack[0])
