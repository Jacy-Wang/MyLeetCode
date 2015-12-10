class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = 0
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for char in word:
            if char not in p.children:
                p.children[char] = TrieNode()
            p = p.children[char]
        p.value = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for char in word:
            if char not in p.children:
                return False
            else:
                p = p.children[char]
        return True if p.value == 1 else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for char in prefix:
            if char not in p.children:
                return False
            else:
                p = p.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
