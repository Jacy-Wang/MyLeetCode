class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0:
            return True
        graph = [[] for _ in xrange(numCourses)]
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        inDegree = [0 for _ in xrange(numCourses)]
        for courses in graph:
            for v in courses:
                inDegree[v] += 1
        q = []
        for i in xrange(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        counter = 0
        while q:
            top = q.pop(0)
            counter += 1
            for v in graph[top]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
        return True if counter == numCourses else False
