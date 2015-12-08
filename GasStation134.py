class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalResidual = 0
        curResidual = 0
        start = 0
        for i in xrange(start, len(cost)):
            tmp = gas[i] - cost[i]
            totalResidual += tmp
            curResidual += tmp
            if curResidual < 0:
                curResidual = 0
                start = i + 1
        if totalResidual < 0:
            return -1
        return start
