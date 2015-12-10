ass Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        if len(grid) == 0:
            return num
        self.r = len(grid)
        self.c = len(grid[0])
        self.grid = grid
        self.visited = [[False for _ in xrange(self.c)] for _ in xrange(self.r)]
        for i in xrange(self.r):
            for j in xrange(self.c):
                if grid[i][j] == '1' and not self.visited[i][j]:
                    num += 1
                    self.visited[i][j] = True
                    self.bfs((i, j))
        return num
                
    def bfs(self, point):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = []
        q.append(point)
        while q:
            top = q.pop(0)
            for d in directions:
                neighbor = (top[0] + d[0], top[1] + d[1])
                if self.isValid(neighbor) and self.grid[neighbor[0]][neighbor[1]] == '1' and not self.visited[neighbor[0]][neighbor[1]]:
                    self.visited[neighbor[0]][neighbor[1]] = True
                    q.append(neighbor)
                    self.bfs(neighbor)
                    
    def isValid(self, point):
        if 0 <= point[0] < self.r and 0 <= point[1] < self.c:
            return True
        return False
