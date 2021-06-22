# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    marked = set()
    for i in range(len(A)):
        if A[i] <= X:
            marked.add(A[i])
            if len(marked) == X:
                return i

    return  -1
