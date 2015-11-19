class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        self.matrix = matrix
        self.target = target
        sign, row = self.searchRow(0, len(matrix))
        if sign:
            return False if row == -1 else True
        else:
            self.row = row
            return self.searchCol(0, len(matrix[row]))
     
    def searchCol(self, start, end):
        print start, end, self.matrix[self.row][start], self.matrix[self.row][end - 1]
        if start < end:
            if start == end - 1:
                return False
            elif start == end - 2:
                if self.matrix[self.row][end - 1] == self.target:
                    return True
                else:
                    return False
            else:
                mid = (start + end) / 2
                if self.matrix[self.row][mid] == self.target:
                    return True
                elif self.matrix[self.row][mid] < self.target:
                    return self.searchCol(mid, end)
                else:
                    return self.searchCol(start, mid)
                
    def searchRow(self, start, end):
        if start < end:
            if start == end - 1:
                if self.matrix[start][0] == self.target:
                    return 1, start
                elif self.matrix[start][0] > self.target:
                    return 1, start - 1
                else:
                    return 0, start
            else:
                if self.matrix[start][0] == self.target:
                    return 1, start
                elif self.matrix[end - 1][-1] == self.target:
                    return 1, end - 1
                elif self.matrix[start][0] > self.target or self.matrix[end - 1][-1] < self.target:
                    return 1, -1
                else:
                    if start == end - 2:
                        if self.matrix[end - 1][0] == self.target:
                            return 1, end - 1
                        elif self.matrix[end - 1][0] < self.target:
                            return 0, end - 1
                        else:
                            return 0, start
                    else:
                        mid = (start + end) / 2
                        if self.matrix[mid][0] == self.target:
                            return 1, mid
                        elif self.matrix[mid][0] < self.target:
                            return self.searchRow(mid, end)
                        else:
                            return self.searchRow(start, mid)
