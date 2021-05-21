'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = {n} # cycle이라는 set 자료형을 사용함으로써 중복을 배제함
        times = 1

        while n != 1:
            n = self.generator(n)
            cycle.add(n)
            times += 1
            if times != len(cycle): # 중복된 숫자가 있다면 cycle이 생겼다는 의미
                return False

        return True

    def generator(self, n: int): # 숫자 n을 각 자릿수의 합으로 바꿔주는 함수
        result = 0
        n = list(str(n))
        for num in n:
            result += int(num) ** 2

        return result