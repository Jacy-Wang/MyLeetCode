import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        numHeap = []
        heapq.heappush(numHeap, 1)
        for _ in xrange(n):
            curNum = heapq.heappop(numHeap)
            if curNum % 2 == 0:
                heapq.heappush(numHeap, curNum * 2)
            elif curNum % 3 == 0:
                heapq.heappush(numHeap, curNum * 2)
                heapq.heappush(numHeap, curNum * 3)
            else:
                heapq.heappush(numHeap, curNum * 2)
                heapq.heappush(numHeap, curNum * 3)
                heapq.heappush(numHeap, curNum * 5)
        return curNum
