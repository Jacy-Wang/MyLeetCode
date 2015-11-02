class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = '1'
        for i in xrange(2, n + 1):
            res = ""
            prev = seq[0]
            counter = 1
            for j in xrange(1, len(seq)):
                if seq[j] == prev:
                    counter = counter + 1
                else:
                    res = res + str(counter) + prev
                    prev = seq[j]
                    counter = 1
            seq = res + str(counter) + prev
        return seq
