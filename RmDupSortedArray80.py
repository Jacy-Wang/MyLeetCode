class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos1 = 0
        pos2 = 0
        counter = 1
        numsLen = len(nums)
        for i in xrange(1, numsLen):
            if pos1 == 0:
                if nums[i] == nums[i - 1]:
                    counter += 1
                    if counter == 3:
                        pos1 = i
                        val = nums[pos1]
                else:
                    counter = 1
            else:
                if counter >= 2:
                    for j in xrange(pos2, numsLen):
                        if nums[j] > val:
                            pos2 = j + 1
                            nums[pos1] = nums[j]
                            val = nums[pos1]
                            pos1 += 1
                            counter = 1
                            break
                    else:
                        return pos1
                else:
                    if pos2 < numsLen:
                        nums[pos1] = nums[pos2]
                        if nums[pos2] == val:
                            counter += 1
                        else:
                            counter = 1
                            val = nums[pos2]
                        pos1 += 1
                        pos2 += 1
        return pos1 if pos1 else numsLen
