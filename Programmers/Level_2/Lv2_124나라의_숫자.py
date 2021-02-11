'''풀이방법
1 -> 1
2 -> 2
3 -> 4
'''

def solution(n):
    answer = ''

    while n >= 3 :
        if n%3 == 0 :
            n = n/3 - 1
            answer = '4' + answer
        else :
            answer = str(int(n%3)) + answer
            n = int(n/3)

    if n != 0 :
        answer = str(int(n)) + answer

    return answer


'''
def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

좋아요를 가장 많이 받은 코드이다.
문제를 풀면서 처음에는 위의 코드와 같은 방향으로 생각을 했었는데
풀다보니 코드가 산으로 갔다. 
아직도 내가 생각한대로 코드화 하지 못한다는 점에서 많이 부족한 것 같다.
다시 한번 파이썬 리스트의 강력함과 // 연산자를 복습하여 기억해놓아야 겠다.
'''

