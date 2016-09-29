class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        nums = sorted(nums)
        length = [1 for _ in xrange(len(nums))]
        pre = [-1 for _ in xrange(len(nums))]
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i] % nums[j] == 0:
                    if length[j] + 1 > length[i]:
                        pre[i] = j
                        length[i] = length[j] + 1
        idx = length.index(max(length))
        res = []
        while idx >= 0:
            res.append(nums[idx])
            idx = pre[idx]
        return res
