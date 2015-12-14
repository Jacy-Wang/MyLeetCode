class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        nums = sorted(citations, reverse = True)
        accumulator = 0
        h = len(nums)
        i = 0
        while i < len(nums) and h >= 0:
            if nums[i] >= h:
                accumulator += 1
            else:
                if accumulator >= h:
                    return h
                else:
                    h -= 1
                    i -= 1
            i += 1
        if accumulator >= h:
            return h
        return 0
