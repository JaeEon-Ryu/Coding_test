class Solution:

    '''
    reference: iamlockon
    '''
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList:
            return []

        found, q, nq = False, {beginWord}, set()
        while q and not found: # 단어를 찾았을 때, 혹은 더이상 찾을 단어가 없을 때까지 반복
            words -= set(q)
            for x in q: # 현재 단계에 존재하는 모든 단어들
                for_each_word = [
                    x[:i]+c+x[i+1:]
                    for i in range(n)
                    for c in 'qwertyuiopasdfghjklzxcvbnm'
                ]

                for y in for_each_word:
                    if y in words:
                        if y == endWord: # 찾았을 경우
                            found = True
                        else:
                            nq.add(y) # 다음 큐 준비
                        tree[x].add(y) # 경로 추가
            q, nq = nq, set() # reset

        def bt(x): # backtracking
            if x == endWord:
                return [[x]]
            else:
                return [
                    [x] + rest for y in tree[x]
                    for rest in bt(y)
                ]

        return bt(beginWord)

    ''' 시간 초과
    import copy

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        self.result = []
        self.endWord = endWord
        self.generator([beginWord], wordList, 2)

        return self.result

    def generator(self, li: List[str], wl: List[str], length: int):
        if self.result and len(self.result[-1]) < length:
            return

        for word in wl:
            if self.is_match(li[-1], word):
                temp = copy.deepcopy(wl)
                temp.remove(word)
                self.generator(copy.deepcopy(li) + [word], temp, length + 1)

                if self.endWord == word: # 마지막 단어 완성
                    li.append(word)

                    if not self.result: # 완성된 결과 최초 저장시
                        self.result.append(li)
                    else:
                        if len(self.result[-1]) > length: # 기존 결과보다 더 짧은 경로가 있다면 초기화 후 저장
                            self.result = []
                            self.result.append(li)
                        elif len(self.result[-1]) == length: # 기존 결과와 경로 길이가 같다면 추가하여 저장
                            self.result.append(li)

    def is_match(self, word1: str, word2: str): # 비교 대상이 한글자 빼고 모두 맞는지
        cnt = 0
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                cnt += 1
            if cnt > 1:
                return False
        return True
    '''



