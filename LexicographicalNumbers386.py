class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return []
        res = []
        stack = []
        stack.append(1)
        while stack:
            top = stack.pop()
            if top <= n:
                res.append(top)
                if top % 10 < 9:
                    stack.append(top + 1)
                if top * 10 <= n:
                    stack.append(top * 10)
        return res
