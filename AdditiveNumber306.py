class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        for i in xrange(1, len(num)):
            for j in xrange(i + 1, len(num)):
                s1 = num[: i]
                s2 = num[i : j]
                if (s1.startswith("0") and len(s1) > 1) or (s2.startswith("0") and len(s2) > 1):
                    continue
                k = j
                while k < len(num):
                    s3 = str(int(s1) + int(s2))
                    if not num.startswith(s3, k):
                        break
                    s1 = s2
                    s2 = s3
                    k += len(s3)
                if (k == len(num)):
                    return True
        return False
