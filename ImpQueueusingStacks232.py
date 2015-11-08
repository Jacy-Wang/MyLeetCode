class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1, self.stack2 = Queue.transfer(self.stack1, self.stack2)
        self.stack2.append(x)
        self.stack2, self.stack1 = Queue.transfer(self.stack2, self.stack1)

    @staticmethod
    def transfer(a, b):
        while len(a):
            item = a.pop()
            b.append(item)
        return a, b

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack1.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0
