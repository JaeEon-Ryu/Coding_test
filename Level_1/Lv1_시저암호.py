def solution(s, n):
    answer = ''

    for idx, char in enumerate(s):
        shifted = chr(ord(char) + n)

        if char >= 'a':
            if shifted > 'z':
                answer += chr(ord(shifted) - 26)
            else:
                answer += shifted

        elif char >= 'A':
            if shifted > 'Z':
                answer += chr(ord(shifted) - 26)
            else:
                answer += shifted

        else:
            answer += char

    return answer