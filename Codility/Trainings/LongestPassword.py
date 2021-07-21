# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    '''
        문자의 개수 : 짝수
        숫자의 개수 : 홀수
    '''

    def valid_len(text):
        letter_size, digit_size = 0, 0

        for t in text:
            if t.isalpha():
                letter_size += 1
            elif t.isdigit():
                digit_size += 1
            else:
                return -1

        return len(text) if letter_size % 2 == 0 and digit_size % 2 == 1 else -1

    longest_pw = -1
    for s in S.split():
        longest_pw = max(longest_pw, valid_len(s))

    return longest_pw
