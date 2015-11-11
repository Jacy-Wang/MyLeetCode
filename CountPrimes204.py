class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True for _ in xrange(n)]
        i = 2
        while i * i < n:
            for j in xrange(i * i, n, i):
                isPrime[j] = False
            i = i + 1
        counter = 0
        for i in xrange(2, n):
            if isPrime[i]:
                counter = counter + 1
        return counter
