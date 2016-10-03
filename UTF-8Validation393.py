class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        counter = 0
        i = 0
        while i < len(data):
            if data[i] >= 255:
                return False
            while (data[i] >> (7 - counter)) & 1 == 1:
                counter += 1
            if counter == 1:
                return False
            elif counter == 0:
                i += 1
                continue
            if i + counter > len(data):
                return False
            for j in xrange(i + 1, i + counter):
                if not self.check(data[j]):
                    return False
            i += counter
            counter = 0
        return True

    def check(self, num):
        return (num >> 7) & 1 == 1 and (num >> 6) & 1 == 0
