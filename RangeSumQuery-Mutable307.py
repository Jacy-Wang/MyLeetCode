class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.partialSum = [0 for _ in xrange(len(nums) + 1)]
        for i in xrange(1, len(self.partialSum)):
            for j in xrange(i - self.lowbit(i) + 1, i + 1):
                self.partialSum[i] += self.nums[j - 1]

    def lowbit(self, num):
        return -num & num

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        j = i + 1
        while j < len(self.partialSum):
            self.partialSum[j] += (val - self.nums[i])
            j += self.lowbit(j)
        self.nums[i] = val

    def prefixSum(self, k):
        res = 0
        i = k
        while i > 0:
            res += self.partialSum[i]
            i -= self.lowbit(i)
        return res

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefixSum(j + 1) - self.prefixSum(i)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
