class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        d = dict()
        for c in ransomNote:
            d[c] = d.get(c, 0) + 1
        for c in magazine:
            if c in d.keys():
                d[c] -= 1
        for key, val in d.items():
            if val > 0:
                return False
        return True
