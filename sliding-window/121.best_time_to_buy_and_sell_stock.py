class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        best_profit = 0 # default return, and deals with improper arrays

        # sliding window/two pointers happening
        while right < len(prices):
            if prices[left] < prices[right]:
                curr_profit = prices[right] - prices[left]
                best_profit = max(best_profit, curr_profit)
            else: # this is the element that matters really, because it improves out time complexity
                left = right
            # always iterating to the right
            right += 1

        return best_profit
            



 
