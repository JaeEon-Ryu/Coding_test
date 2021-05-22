'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        1. 지우게 되는 인덱스가 s와 t 둘 다 같아야함
        2. 해당 인덱스 값과 같은 모든 값들을 지워야 함
        '''

        while s and t:
            temp_1 = []
            for idx, sub_s in enumerate(s):
                if sub_s == s[0]:
                    temp_1.append(idx)

            temp_2 = []
            for idx, sub_t in enumerate(t):
                if sub_t == t[0]:
                    temp_2.append(idx)

            if temp_1 != temp_2:
                return False

            s = s.replace(s[0], '')
            t = t.replace(t[0], '')

        return True


'''
다른 사람의 풀이 : OldCoadingFarmer - dict자료형을 이용하려 풀이함
   def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
'''