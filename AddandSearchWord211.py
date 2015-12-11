class Node(object):
    def __init__(self):
        self.val = 0
        self.children = [None for _ in xrange(26)]

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p = self.root
        for char in word:
            if not p.children[ord(char) - 97]:
                p.children[ord(char) - 97] = Node()
            p = p.children[ord(char) - 97]
        p.val = 1

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        p = self.root
        self.word = word
        return self.recursiveSearch(0, p)

    def recursiveSearch(self, pos, head):
        if pos == len(self.word):
            if head.val == 1:
                return True
            else:
                return False
        else:
            if self.word[pos] == '.':
                for v in head.children:
                    if v and self.recursiveSearch(pos + 1, v):
                        return True
                return False
            else:
                cur = head.children[ord(self.word[pos]) - 97]
                if cur:
                    return self.recursiveSearch(pos + 1, cur)
                else:
                    return False
