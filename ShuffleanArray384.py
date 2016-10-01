class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        tmp = self.nums[:]
        res = [0 for _ in xrange(len(self.nums))]
        for i in xrange(len(res)):
            val = random.randint(0, len(tmp) - 1)
            res[i] = tmp[val]
            tmp[val] = tmp[len(tmp) - 1]
            tmp.pop()
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
