
from itertools import product
import itertools

def solution(user_id, banned_id):

    possible_cases = [] # banned_id의 입장에서 user_id가 될 수 있는 모든 문자 저장

    for b_id in banned_id:
        is_possible = []

        for u_id in user_id:
            if len(b_id) == len(u_id):
                same = True

                for b_char,u_char in zip(b_id,u_id):

                    if b_char != '*' and b_char != u_char:
                        same = False
                        break

                if same:
                    is_possible.append(u_id)

        possible_cases.append(is_possible)

    num_of_cases = list(product(*possible_cases)) # possible_cases 카테시안곱

    answer_list = []
    for case in num_of_cases:
        if len(set(case)) == len(banned_id):
            answer_list.append(sorted(case))
            '''
                ('frodo', 'crodo', 'abc123', 'frodoc')
                ('frodo', 'crodo', 'frodoc', 'abc123')
                위의 두 결과는 같은 결과임 -> 중복 제거해야함
                
                중복 제거 과정 - 리스트에 값이 없다면 저장 
                -> 이런식으로 하면 테스트5틀림
                
                -> 튜플로 변환 후 set으로 중복 제거한 다음 길이 구하기
            '''

    return len(list(set(map(tuple, answer_list))))

#user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
#banned_id = ["fr*d*", "abc1**"]

#user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
#banned_id = ["*rodo", "*rodo", "******"]

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id,banned_id))