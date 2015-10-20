class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsLength = len(nums)
        tupleNums = [(nums[i], i + 1) for i in xrange(numsLength)]
        sortedTupleNums = sorted(tupleNums, key = lambda tup : tup[0])
        self.sortedTupleNums = sortedTupleNums
        for i in xrange(numsLength - 1):
            residual = target - sortedTupleNums[i][0]
            interRes = self.findNum(i + 1, numsLength - 1, residual)
            if interRes > 0:
                return sorted([sortedTupleNums[i][1], sortedTupleNums[interRes][1]])

    def findNum(self, start, end, residual):
        
        if start <= end:
            middle = int((start + end)/2)
            if self.sortedTupleNums[middle][0] == residual:
                return middle
            elif self.sortedTupleNums[middle][0] < residual:
                return self.findNum(middle + 1, end, residual)
            else:
                return self.findNum(start, middle - 1, residual)
        else:
            return -1
