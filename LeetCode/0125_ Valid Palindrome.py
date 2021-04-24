'''
Given a string s, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
'''

'''
숫자이거나 알파벳인 것만 추출
대소문자 구별해야함 
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for str_s in s:
            if 48 <= ord(str_s) <= 57 or 65 <= ord(str_s) <= 90 or 97 <= ord(str_s) <= 122:
                new_s += str_s

        new_s = new_s.lower()

        return new_s == new_s[::-1]