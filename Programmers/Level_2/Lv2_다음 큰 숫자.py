def count_binary_1(n): # 10진수에서 2진수로 바꾸고 1 count
    result = ''

    while n>0:
        result += str(n%2)
        n//=2

    # 연산결과 result[::-1]을 해주거나 큐를 이용해야하지만 1의 개수를 세는 것 말고는
    # 다른 기능을 필요로 하지 않아서 바로 리턴
    return result.count('1')

def solution(n):

    original = count_binary_1(n)
    up = 1
    while original != count_binary_1(n + up):
        up += 1

    return n + up

print(solution(78))