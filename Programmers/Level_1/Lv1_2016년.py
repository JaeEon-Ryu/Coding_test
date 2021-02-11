import time
import datetime

def solution(a, b):
    answer = ''
    d = datetime.datetime(2016, a, b)
    answer = (str(d.strftime('%a')))
    return answer.upper()