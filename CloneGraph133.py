# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return node
        newHead = UndirectedGraphNode(node.label)
        nodeDict = {}
        nodeDict[node] = newHead
        q = []
        q.append(node)
        while q:
            top = q.pop(0)
            for v in top.neighbors:
                if v in nodeDict.keys():
                    nodeDict[top].neighbors.append(nodeDict[v])
                else:
                    curNeighbor = UndirectedGraphNode(v.label)
                    nodeDict[v] = curNeighbor
                    nodeDict[top].neighbors.append(curNeighbor)
                    q.append(v)
        return newHead
