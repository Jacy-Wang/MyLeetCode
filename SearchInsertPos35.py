ss Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = nums
        self.target = target
        numsLen = len(nums)
        return self.find(0, numsLen - 1)

    def find(self, left, right):
        if right > left:
            mid = (left + right) / 2
            if self.nums[mid] == self.target:
                return mid
            elif self.nums[mid] > self.target:
                if right == left + 1:
                    return left
                else:
                    return self.find(left, mid)
            else:
                if right == left + 1:
                    if self.nums[right] >= self.target:
                        return right
                    else:
                        return right + 1
                else:
                    return self.find(mid, right)
        elif right == left:
            return left if self.nums[left] >= self.target else left + 1
