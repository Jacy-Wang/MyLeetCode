class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        heap = []
        for i in xrange(len(nums1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        res = []
        while len(res) < k and len(res) < len(nums1) * len(nums2):
            top = heapq.heappop(heap)
            res.append([nums1[top[1]], nums2[top[2]]])
            if top[2] + 1 < len(nums2):
                heapq.heappush(heap, (nums1[top[1]] + nums2[top[2] + 1], top[1], top[2] + 1))
        return res
