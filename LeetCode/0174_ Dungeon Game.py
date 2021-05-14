class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''
        reference : sengoku
        '''
        dp = [
            [0] * len(dungeon[0])
            for i in range(len(dungeon))
        ]

        # 도착지점에 있는 숫자가 양수라면 hp가 1만 있어도 된다.
        # 도착지점에 있는 숫자가 음수라면 그 숫자에 상응하는 절대값(양수)보다 1이 더 커야함
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])

        # 세로
        for i in range(len(dungeon) - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])
        # 가로
        for j in range(len(dungeon[0]) - 2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j + 1] - dungeon[-1][j])

        for i in range(len(dungeon) - 2, -1, -1):
            for j in range(len(dungeon[0]) - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j] - dungeon[i][j],
                                      dp[i][j + 1] - dungeon[i][j]))

        '''
        -2 -3 3
        -5 -10 1
        10 30 -5
        
        7 5 2
        6 11 5
        1 1 6
        '''

        return dp[0][0]