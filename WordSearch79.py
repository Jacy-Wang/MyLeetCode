class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        self.board = board
        self.word = word
        self.movement = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if self.check((i, j), [], 0):
                    return True
        return False
        
    def check(self, pair, paths, pos):
        if pos == len(self.word):
            return True
        else:
            if not self.isValid(pair) or pair in paths or self.word[pos] != self.board[pair[0]][pair[1]]:
                return False
            else:
                for m in self.movement:
                    neighbor = (pair[0] + m[0], pair[1] + m[1])
                    if self.check(neighbor, paths + [pair], pos + 1):
                        return True
                return False
    
    def isValid(self, neighbor):
        return 0 <= neighbor[0] < len(self.board) and 0 <= neighbor[1] < len(self.board[0])
