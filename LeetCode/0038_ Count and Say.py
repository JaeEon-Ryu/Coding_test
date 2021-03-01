class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        saying = self.countAndSay(n-1)
        result = ''
        last_char = saying[0]
        last_count = 0

        for ch in saying:
            if ch == last_char :
                last_count += 1
            else:
                result += str(last_count) + last_char
                last_char = ch
                last_count = 1

        result += str(last_count) + last_char

        return result

solution = Solution()
n = 4
print(solution.countAndSay(n))

'''
1 -> 1
2 -> 1 -> 11
3 -> 11 -> 21
4 -> 21 -> 1211
5 -> 4 -> 41

'''