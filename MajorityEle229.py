class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        e1, e2 = 0, 0
        number1, number2 = 0, 0
        for v in nums:
            if v == e1:
                number1 += 1
            elif v == e2:
                number2 += 1
            elif number1 == 0:
                e1 = v
                number1 = 1
            elif number2 == 0:
                e2 = v
                number2 = 1
            else:
                number1 -= 1
                number2 -= 1
        number1, number2 = 0, 0
        for v in nums:
            if v == e1:
                number1 += 1
            elif v == e2:
                number2 += 1
        res = []
        if number1 > len(nums) / 3:
            res.append(e1)
        if number2 > len(nums) / 3:
            res.append(e2)
        return res
