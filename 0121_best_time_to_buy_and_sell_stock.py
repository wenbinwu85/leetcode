from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            try:
                if price < prices[i+1]:
                    max_price = max(prices[i:])
                    current_profit = max_price - price
                    max_profit = max(max_profit, current_profit)
            except IndexError:
                break
        return max_profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    answer = Solution().maxProfit(prices)
    print(answer)
