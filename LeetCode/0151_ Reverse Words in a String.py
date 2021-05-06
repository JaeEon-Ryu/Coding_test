'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

'''
문자열의 문자들을 하나씩 검사
문자가 만약 공백이라면 그 앞에 해당하는 단어들을 새로운 리스트에 저장
저장된 리스트를 문자형으로 변환하며 각 단어 사이에 공백을 줌
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s += ' '
        non_space_s = []

        is_written = False
        sub_s = ''
        for char in s:
            if char != ' ': # 문자일 경우
                sub_s += char
                is_written = True
            else: # 공백일 경우
                if is_written: # 앞에 단어가 있다면
                    non_space_s.append(sub_s)
                    is_written = False
                    sub_s = ''

        return ' '.join(non_space_s[::-1])

