
'''
맨 아래 풀이 방법 -> 탐색방법이 잘못되었음. ( 테스트 케이스에만 치중함 )
정해진 문자열안에 여러개의 palindrome이 있을 수 있음에 유의하며 풀어야한다.

솔루션 :
리스트의 처음부터 탐색. 해당 문자와 같은 문자가 리스트에 있다면 그 문자들을
따로 저장해둠 ( idx_list_of_same_values ) 그 후, 저장된 문자들로 반복문을
돌려서 인덱스 슬라이싱을 통해 같은 문장인지 판별 ( is_palindrome ).

비교 방법 ( is_palindrome ):
어떠한 문장이 제시되었을 때
그 길이가 홀수라면 가운데를 빼고 서로 비교
짝수라면 가운데를 빼지 않고 서로 비교
--> 왼쪽 문자열 == 뒤집힌 오른쪽 문자열

다른 사람 풀이를 보고 난 후 :
따로 is_palindrome()이라는 함수를 만들 필요가 없음
그냥 리스트 == 리스트[::-1] 하면 된다
'''

import math

def is_palindrome(s):

    left = s[:len(s)//2]
    right = s[math.ceil(len(s)/2):]
    right_reversed = right[::-1]

    return True if left == right_reversed else False

def idx_list_of_same_values(list,idx):

    original_value = list[idx]
    result = []
    idx += 1

    while idx < len(list):
        if list[idx] == original_value:
            result.append(idx)
        idx += 1

    return result[::-1] # 내림차순


def solution(s):

    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            print(i,' ',j)
            if s[j:j + i] == s[j:j + i][::-1]:
                print(s[j:j + i],' ',s[j:j + i][::-1])
                return i
    # answer = 0
    # idx = 0
    #
    # while idx < len(s)-1:
    #     if s[idx] in s[idx+1:]:
    #         cases = idx_list_of_same_values(s,idx)
    #
    #         for c in cases: # 같은 문자가 있는 인덱스들
    #
    #             if is_palindrome(s[idx:c+1]):
    #                 if answer < c+1 - idx:
    #                     answer = c+1 - idx
    #                 break
    #
    #     idx += 1
    #
    # return answer



'''
def solution(s):

    idx_change = 0
    while idx_change < len(s):
        start_from_left = s[idx_change:]
        start_from_right = s[:len(s) - idx_change]

        if is_palindrome(start_from_left) or is_palindrome(start_from_right):
            return len(s) - idx_change

        idx_change += 1

    return 0
'''

#s = "abccbaz"
s = 'ababaz'
s3 = '우리집강아지으르렁렁르으우리집고양이야옹야옹옹야옹야'
print(solution(s))
