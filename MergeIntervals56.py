# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        sortedIntervals = self.sort(intervals)
        start = sortedIntervals[0].start
        latest = sortedIntervals[0].end
        res = []
        for i in xrange(1, len(sortedIntervals)):
            if sortedIntervals[i].start > latest:
                res.append(Interval(start, latest))
                start = sortedIntervals[i].start
                latest = sortedIntervals[i].end
            else:
                latest = max(latest, sortedIntervals[i].end)
        res.append(Interval(start, latest))
        return res

    def sort(self, intervals):
        hq = []
        for i in xrange(len(intervals)):
            heapq.heappush(hq, (intervals[i].start, intervals[i]))
        sortedIntervals = []
        while hq:
            item = heapq.heappop(hq)
            sortedIntervals.append(item[1])
        return sortedIntervals
