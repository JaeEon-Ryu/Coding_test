'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''

'''
해쉬 테이블 사용
'''
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.word_dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        words = self.word_dict[len(word)]
        for i, char in enumerate(word):
            words = [w for w in words if char in ['.', w[i]]]
            if not words:
                return False
        return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)