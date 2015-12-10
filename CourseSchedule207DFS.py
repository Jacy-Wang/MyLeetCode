class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0:
            return True
        self.graph = [[] for _ in xrange(numCourses)]
        for pair in prerequisites:
            if pair[0] not in self.graph[pair[1]]:
                self.graph[pair[1]].append(pair[0])
        self.visited = [0 for _ in xrange(numCourses)]
        for i in xrange(numCourses):
            if self.visited[i] != 1:
                if not self.dfs(i):
                    return False
        return True

    def dfs(self, i):
        if self.visited[i] == 1:
            return True
        else:
            self.visited[i] = -1
            for course in self.graph[i]:
                if self.visited[course] == -1 or not self.dfs(course):
                    return False
            self.visited[i] = 1
            return True
