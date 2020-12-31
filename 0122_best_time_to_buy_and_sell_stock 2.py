from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for idx, price in enumerate(prices):
            try:
                if price < prices[idx+1]:
                    total_profit += prices[idx+1] - price
            except IndexError:
                break
        return total_profit


if __name__ == '__main__':
    prices = [1, 2, 3, 4, 5]
    answer = Solution().maxProfit(prices)
    print(answer)
