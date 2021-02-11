# 주어진 리스트 원소를 하나 뽑아서
# 나머지 원소들과 비교 후 prefix가 맞다면
# false를 리턴, prefix가 없다면 true를 리턴한다.
#
# [ 123, 1, 312 ]

def solution(phone_book):
    phone_book.sort()
    prefix = phone_book.pop(0)
    for num in phone_book :
        if prefix in num :
            return False
    return True

#
# 비교적 간단하게 풀었다.
# 정렬후에 제일 작은 숫자를 뽑아서
# 반복문을 돌려 in 함수로 정해진 원소가 포함되어
# 있는지 검사한다.
# 검사해서 있다면 False
# 없다면 True 반환