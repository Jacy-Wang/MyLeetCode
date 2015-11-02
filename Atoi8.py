class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip(' ')
        opSign = False
        op = ['-', '+']
        for i in xrange(len(str)):
            if i == 0:
                if str[i] < '0' or str[i] > '9':
                    if str[i] not in op:
                        return 0
                    else:
                        opSign = True
            elif i == 1:
                if str[i] < '0' or str[i] > '9':
                    if opSign:
                        return 0
                    else:
                        return int(str[: i])
            else:
                if str[i] < '0' or str[i] > '9':
                    return Solution.decide(str[: i])
        if len(str) == 0:
            return 0
        elif len(str) == 1 and opSign:
            return 0
        else:
            return Solution.decide(str)
            
    @staticmethod
    def decide(s):
        if int(s) > 2147483647:
            return 2147483647
        elif int(s) < -2147483648:
            return -2147483648
        return int(s)
