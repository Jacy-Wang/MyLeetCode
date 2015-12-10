class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in xrange(numCourses)]
        for pair in prerequisites:
            if pair[0] not in graph[pair[1]]:
                graph[pair[1]].append(pair[0])
        inDegree = [0 for _ in xrange(numCourses)]
        for courses in graph:
            for v in courses:
                inDegree[v] += 1
        res = []
        q = []
        for i in xrange(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            top = q.pop(0)
            res.append(top)
            for v in graph[top]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
        return res if len(res) == numCourses else []
