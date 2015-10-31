class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        counter = 0
        secretMatched = [False for _ in xrange(len(guess))]
        guessMatched = [False for _ in xrange(len(guess))]
        for i in xrange(min(len(secret), len(guess))):
            if secret[i] == guess[i]:
                counter = counter + 1
                secretMatched[i] = guessMatched[i] = True
        res = "%dA" % counter
        counter = 0
        for i in xrange(len(secret)):
            if not secretMatched[i]:
                for j in xrange(len(guess)):
                    if not guessMatched[j] and guess[j] == secret[i]:
                        counter = counter + 1
                        guessMatched[j] = True
                        break
        return res + "%dB" % counter
