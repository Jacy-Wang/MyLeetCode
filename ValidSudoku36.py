class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #print board
        for i in xrange(9):
            if not Solution.check(board[i]):
                return False
            if not Solution.check(zip(*board)[i]):
                return False
        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                target = board[i][j : j + 3] + board[i + 1][j : j + 3] + board[i + 2][j : j + 3]
                if not Solution.check(target):
                    return False
        return True

    @staticmethod
    def check(lst):
        num = lst.count('.')
        return len(lst) == len(set(lst)) if num < 1 else len(lst) - num + 1 == len(set(lst))
