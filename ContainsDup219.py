class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        numsLen = len(nums) 
        lst = sorted(zip(nums, range(numsLen)))
        val = lst[0][0]
        indices = [lst[0][1]]
        for i in xrange(1, numsLen):
            if lst[i][0] == val:
                for index in indices:
                    if -k <= lst[i][1] - index <= k:
                        return True
                indices.append(lst[i][1])
            else:
                val = lst[i][0]
                indices = [lst[i][1]]
        return False
