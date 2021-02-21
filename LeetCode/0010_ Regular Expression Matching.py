class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # 참고 : Solution , 재귀, dp, top-down 풀이법

        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    # p의 부분 문자가 s의 부분문자와 같거나,
                    # p의 문자가 .인 경우 ( .은 모든 것을 대체 가능 )
                    f_match = i < len(s) and p[j] in {s[i], '.'}

                    # p가 *일 경우 다음 p의 원소를 참고하며 f_match와 or 연산
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or f_match and dp(i + 1, j)
                    else:
                        ans = f_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

