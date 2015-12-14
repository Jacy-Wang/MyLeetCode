class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.board = board
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                liveNeighbors = 0
                for movement in d:
                    liveNeighbors += self.isLiving(i + movement[0], j + movement[1])
                if liveNeighbors == 3 or liveNeighbors + board[i][j] == 3:
                    self.board[i][j] |= 2
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.board[i][j] >>= 1

    def isLiving(self, x, y):
        if x < 0 or x >= len(self.board) or y < 0 or y >= len(self.board[0]):
            return 0
        return self.board[x][y] & 1
