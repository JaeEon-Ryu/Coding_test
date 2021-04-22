'''
ou are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

'''
bought << 구매한 가격
profit << 최대 이익

구매한 가격과 다른 가격을 비교하며 적자가 났다면 구매한 가격 갱신
그 외에는 최대이익 계속 저장
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        bought = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if bought > prices[i]: # 적자
                bought = prices[i]
            else:
                profit = max(profit, prices[i] - bought)

        return profit