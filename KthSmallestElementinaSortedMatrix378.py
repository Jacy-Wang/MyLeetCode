class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        self.rowNum = len(matrix)
        self.colNum = len(matrix[0])
        sign = [[0 for _ in xrange(self.colNum)] for _ in xrange(self.rowNum)]
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        sign[0][0] = 1
        counter = 0
        while counter < k:
            top = heapq.heappop(heap)
            counter += 1
            if self.isValid(top[1] + 1, top[2]) and sign[top[1] + 1][top[2]] == 0:
                heapq.heappush(heap, (matrix[top[1] + 1][top[2]], top[1] + 1, top[2]))
                sign[top[1] + 1][top[2]] = 1
            if self.isValid(top[1], top[2] + 1) and sign[top[1]][top[2] + 1] == 0:
                heapq.heappush(heap, (matrix[top[1]][top[2] + 1], top[1], top[2] + 1))
                sign[top[1]][top[2] + 1] = 1
        return top[0]

    def isValid(self, i, j):
        return 0 <= i < self.rowNum and 0 <= j < self.colNum
