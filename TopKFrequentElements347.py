class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqMap = {}
        for v in nums:
            freqMap[v] = freqMap.get(v, 0) + 1
        bucket = [[] for _ in xrange(len(nums) + 1)]
        for key, val in freqMap.items():
            bucket[val].append(key)
        res = []
        for v in bucket[: : -1]:
            if v:
                length = min(k - len(res), len(v))
                res.extend(v[ : length])
            if len(res) == k:
                return res
