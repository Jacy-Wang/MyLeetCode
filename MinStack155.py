class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVal = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.minVal or x <= self.minVal[-1]:
            self.minVal.append(x)
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: nothing
        """
        val = self.stack.pop()
        if val == self.minVal[-1]:
            self.minVal.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal[-1]
