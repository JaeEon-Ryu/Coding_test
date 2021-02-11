'''
문제를 잘못 이해했다. 연속된 문자가 나오면 쭉 지우는 줄 알았는데
문제의 제목처럼 짝을 지어 제거하는 것이다.
다시말해서 두개이상의 연속된 문자가 나와도 2개만 제거하는 것이라 보면 된다.
'''

def solution(s):

    answer = []
    for chr in s:
        if not answer or answer[-1] != chr:
            answer.append(chr)
        else:
            answer.pop()

    if answer:
        return 0
    else:
        return 1

# def solution(s):
#
#     s = list(s)
#     loop = True
#
#     while loop:
#         loop = False
#         preceding_char = '0'
#
#         for idx,char in enumerate(s):
#             if preceding_char == char:
#                 loop = True
#                 plus = 0
#
#                 while idx+plus < len(s) and preceding_char == s[idx+plus]:
#                     plus += 1
#                 else:
#                     del s[idx-1:idx+plus]
#                     break
#
#             preceding_char = char
#
#     if not s:
#         return 1
#     else:
#         return 0

print(solution('baabaa'))