'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
'''

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        sub = ""
        for w in word:
            sub += w
            if sub not in self.tree:
                self.tree[sub] = 1
        self.tree[word] = 2

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.tree and self.tree[word] == 2:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return prefix in self.tree

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)