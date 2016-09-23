class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.partialSum = [0 for _ in xrange(len(self.nums) + 1)]
        for i in xrange(1, len(self.partialSum)):
            self.partialSum[i] = self.partialSum[i - 1] + self.nums[i - 1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.partialSum[j + 1] - self.partialSum[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
