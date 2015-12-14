class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        val = ""
        for i in xrange(len(input)):
            if input[i].isdigit():
                val += input[i]
            else:
                break
        if i == len(input) - 1:
            return [int(val)]
        res = []
        for i in xrange(len(input)):
            if not input[i].isdigit():
                left = self.diffWaysToCompute(input[: i])
                right = self.diffWaysToCompute(input[i + 1 :])
                for l in left:
                    for r in right:
                        res.append(self.calculate(l, r, input[i]))
        return res
                        
    def calculate(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
