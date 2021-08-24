def solution(price, money, count):
    for c in range(1, count + 1):
        money -= price * c

    return money * -1 if money < 0 else 0