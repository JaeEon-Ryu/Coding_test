# 원래 최초의 코드는 if 문자열 in 문자열 같은 구문으로 만들었다.
# 하지만 중복된 이름이 있는 케이스 때문에 오답이 나왔다.
# 따라서 예외사항을 두었으나 쉬운 문제에 비해 코드가 너무 길고 보기 난잡해져
# 다른 방법인 zip 함수를 사용하여 풀었다.

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p != c :
            return p
    return participant[-1]

# zip()이란? - 동일한 개수로 이루어진 두 자료형을 순서대로 짝지어 튜플로 묶어주는 함수.
