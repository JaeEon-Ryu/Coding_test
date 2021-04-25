'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
'''

class Solution:
    '''
    reference : kevined51
    '''
    wordList = set(wordList)
    queue = collections.deque([[beginWord, 1]])  # 단어와 거쳐온 경로의 개수 저장

    while queue:
        word, length = queue.popleft()
        if word == endWord:  # 제일 먼저 나오는 경로가 제일 짧은 경로임
            return length

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]

                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append([next_word, length + 1])

    return 0

    '''시간초과
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.shortest = len(wordList)
        self.endWord = endWord
        self.found_answer = False
        self.generator(beginWord, wordList, 1)

        return self.shortest if self.found_answer else 0

    def generator(self, current: int, wl: List[str], length: int):
        if self.shortest <= length:
            return

        for word in wl:
            if self.is_match(current, word):
                temp = copy.deepcopy(wl)
                temp.remove(word)
                if self.endWord == word:  # 마지막 단어 완성시
                    self.shortest = min(self.shortest, length + 1)
                    self.found_answer = True
                else:
                    self.generator(word, temp, length + 1)

    def is_match(self, word1: str, word2: str):  # 비교 대상이 한글자 빼고 모두 맞는지
        cnt = 0
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                cnt += 1
            if cnt > 1:
                return False
        return True
    '''