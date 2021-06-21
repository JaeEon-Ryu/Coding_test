# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    quotient,remainder = divmod(Y-X,D)
    return quotient + 1 if remainder else quotient
