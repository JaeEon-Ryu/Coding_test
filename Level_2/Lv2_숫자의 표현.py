def solution(n):
    answer = 0

    for start in range(1,n+1):
        temp = 0
        for num in range(start,n+1):
            temp += num
            if temp == n:
                answer += 1
                break
            if temp > n:
                break

    return answer

n = 15
print(solution(n))

'''
눈여겨볼만한 풀이
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])

수학공식을 이용하여 문제의 복잡도를 줄였음
예를 들어 n이 3개의 연속된 자연수(i-1, i, i+1)의 합으로 표현된다면 합은 3i
즉, n은 3의 배수임. 
마찬가지로 5개의 연속된 자연수의 합으로 n이 표현이 된다면 
n은 5의 배수여야함. 
따라서, n의 약수 중 홀수가 몇개있냐는 문제와 같은 문제로 해석할 수 있음.
dntjr8096―2020.05.16 03:00 코멘트
'''