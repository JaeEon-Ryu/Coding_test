class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # 참고 : Anavil
        from collections import Counter
        from collections import defaultdict
        c = Counter(words)
        words_len = len(words)
        n = len(words[0])
        result = []

        for k in range(n):
            left = k

            word_cnt = 0

            # s에 있는 단어들 탐색
            for j in range(k, len(s) - n + 1, n):
                word = s[j:j + n]

                if word in c:
                    sub_d[word] += 1
                    word_cnt += 1

                    # 예외처리
                    while sub_d[word] > c[word]:
                        sub_d[s[left:left + n]] -= 1
                        left += n
                        word_cnt -= 1

                    if word_cnt == words_len:
                        result.append(left)

                else:
                    left = j + n
                    sub_d = defaultdict(int)
                    word_cnt = 0

        return result

        '''
        시간초과가 났던 코드
        ->  words의 길이가 길어지면 permutation으로 인해
            메모리도 많이 먹게 될 뿐더러, 시간소비가 큼
        
        from itertools import permutations
    
        result = set()
        # permutation in words
        possible_words = list(permutations(words,len(words)))
    
        for word in possible_words:
            # substrings_starting_index
            word = ''.join(word)
            w_len = len(word)
    
            for idx in range(len(s)-w_len+1):
                if s[idx:idx+w_len] == word:
                    result.add(idx)
    
        return list(result)
        '''
