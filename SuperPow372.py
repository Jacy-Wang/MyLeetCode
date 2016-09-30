class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        num = 1337
        pow = a
        res = 1
        for v in b[: : -1]:
            res = (res * (pow ** v % num)) % num
            pow = pow ** 10 % num
        return res
