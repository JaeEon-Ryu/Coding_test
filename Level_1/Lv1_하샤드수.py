def solution(x):
    return x%sum(list(map(int,list(str(x)))))==0

print(solution(10))