import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.res = []
        ans = []
        self.place([], 0)
        for sol in self.res:
            board = []
            for pair in sol:
                line = ""
                for j in xrange(pair[1]):
                    line = line + "."
                line = line + "Q"
                for j in xrange(pair[1] + 1, n):
                    line = line + "."
                board.append(line)
            ans.append(board)
        return ans

    def place(self, curPairs, row):
        if row == self.n:
            self.res.append(curPairs)
        else:
            for i in xrange(self.n):
                if self.isValid(curPairs, (row, i)):
                    tmp = copy.deepcopy(curPairs)
                    tmp.append((row, i))
                    self.place(tmp, row + 1)
                    
    def isValid(self, curPairs, pair):
        for v in curPairs:
            if v[1] == pair[1]:
                return False
            if abs(v[1] - pair[1]) == abs(v[0] - pair[0]):
                return False
        return True
