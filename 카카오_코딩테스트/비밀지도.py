def decimal_to_binary(num,n):
    result = ''
    while num > 0:
        result = str(num%2) + result
        num //= 2

    while len(result) != n:
        result = '0' + result

    return result

def solution(n, arr1, arr2):
    answer = []
    for num1,num2 in zip(arr1,arr2):
        binary_1 = decimal_to_binary(num1,n)
        binary_2 = decimal_to_binary(num2,n)
        is_wall = ''

        for idx in range(n):
            if binary_1[idx] == '1' or binary_2[idx] == '1':
                is_wall += '#'
            else:
                is_wall += ' '
        answer.append(is_wall)

    return answer


n= 6
arr1 = [46,33,33,22,31,50]
arr2 = [27,56,19,14,14,10]
print(solution(n,arr1,arr2))



# 다른 사람의 풀이
# 10진수 -> 2진수 변환 bin()함수 사용
# i|j 를 사용하여 or연산자 사용
# rjust 지정된 수만큼 0붙이기 사용
# 1, 0 을 정해진 문자로 교체

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer