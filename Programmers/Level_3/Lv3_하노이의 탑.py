# 2 -> [[1,2],[1,3],[2,3]]

def solution(n):
    answer = []
    def recursive_hanoi(n,start,mid,end):
        if n == 1:
            answer.append([start,end])
            return
        recursive_hanoi(n-1,start,end,mid)
        answer.append([start,end])
        recursive_hanoi(n-1,mid,start,end)

    recursive_hanoi(n,1,2,3)
    return answer

n = 2
print(solution(n))