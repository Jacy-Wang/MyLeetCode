import Queue
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = Queue.Queue()
        self.queue2 = Queue.Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue2.put_nowait(x)
        self.queue1, self.queue2 = Stack.transfer(self.queue1, self.queue2)
        self.queue1 = self.queue2
        self.queue2 = Queue.Queue()

    @staticmethod
    def transfer(a, b):
        while not a.empty():
            item = a.get_nowait()
            b.put_nowait(item)
        return a, b

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue1.get_nowait()

    def top(self):
        """
        :rtype: int
        """
        item = self.queue1.get_nowait()
        self.push(item)
        return item

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue1.empty()
