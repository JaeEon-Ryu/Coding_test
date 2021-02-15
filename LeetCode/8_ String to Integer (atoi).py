class Solution:
    def myAtoi(self, s: str) -> int:

        idx = 0
        result = ''

        while idx < len(s):

            if s[idx] == ' ':
                if result:  # is_not_empty:
                    break

            if 'A' <= s[idx] <= 'z' or s[idx] == '.':
                break

            if '0' <= s[idx] <= '9':
                result += s[idx]

            if s[idx] in ('+', '-'):
                if '+' in result or '-' in result:
                    break
                if result:  # is_not_empty
                    break

                result += s[idx]

            idx += 1

        if result:
            try:
                result = int(result)
            except:
                return 0
            if result < -2 ** 31:
                return -2 ** 31
            elif result > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return result
        else:
            return 0

