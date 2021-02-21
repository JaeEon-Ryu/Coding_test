class Solution:
    def reverse(self, x: int) -> int:

        reversed = 0
        if str(x)[0] == '-':
            reversed = int(str(x)[1:][::-1]) * -1
        else:
            reversed = int(str(x)[::-1])

        if not (-2 ** 31 <= reversed <= 2 ** 31 - 1):
            return 0
        else:
            return reversed