
def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    b = None
    while A:
        a = A.pop()
        if b == None:
            b = B.pop()

        if a < b:
            answer += 1
            b = None

    return answer

A = [8,8,5,5]
B = [9,6,2,2]
print(solution(A,B))

'''
A에서 나오는 값보다 B에서 나오는 값이 더 커야함
A,B 모두 정렬을 해두었기 때문에 B에서 pop을 했을 경우 최대값으로
A에 있는 값을 비교하며 B의 값이 더 크지 않다면 B의 값 그대로 두고
A의 값만 바꿔가며 비교하면 된다.

아래 코드는 내 코드보다 훨씬 게산측면에서 더 나아보여서 가져왔다.
알고리즘은 반대로 짰으나 로직이 비슷하다. 
아래 코드를 보며 생각이 든것이 그냥 리스트 배열 인덱스에 접근하여 비교하면 되는데
굳이 pop 같은 것들을 쓰며 불필요한 메모리와 시간을 잡아먹는 것이 아닌지 생각했다.

    j = 0
    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1

'''
