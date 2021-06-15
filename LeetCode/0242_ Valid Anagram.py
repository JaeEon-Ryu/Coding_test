'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))

        ''' 해쉬를 사용하여 정렬하지 않고 단어 빈도수를 비교하는 방법도 있음
        
        words = collections.defaultdict(int)
        for word in s: 
            words[word] += 1
        for word in t: 
            words[word] -= 1
        
        for cnt in words.values():
            if cnt != 0 :
                return False
        return True
        
        '''