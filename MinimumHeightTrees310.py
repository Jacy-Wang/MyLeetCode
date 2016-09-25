class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        arr = [[] for _ in xrange(n)]
        for edge in edges:
            arr[edge[0]].append(edge[1])
            arr[edge[1]].append(edge[0])
        d = [len(arr[i]) for i in xrange(n)]
        leaves = []
        for i in xrange(n):
            if d[i] <= 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            while leaves:
                top = leaves.pop(0)
                for v in arr[top]:
                    d[v] -= 1
                    if d[v] == 1:
                        newLeaves.append(v)
            leaves = newLeaves
        return leaves
