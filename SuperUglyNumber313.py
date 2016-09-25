class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        num = [1 for _ in xrange(n)]
        idx = [0 for _ in xrange(len(primes))]
        MAX = 2147483647
        for i in xrange(1, n):
            num[i] = MAX
            for j in xrange(len(primes)):
                num[i] = min(num[i], num[idx[j]] * primes[j])
            for j in xrange(len(primes)):
                if num[i] == num[idx[j]] * primes[j]:
                    idx[j] += 1
        return num[n - 1]
