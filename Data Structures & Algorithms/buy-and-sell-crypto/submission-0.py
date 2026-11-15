class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0 

        left, right = 0, 0
        minprice = prices[0]

        for left in range(len(prices)):
        
            if prices[left] > minprice:
                continue 

            right = left

            while right < len(prices):
                print('buying at', prices[left])
                currprofit = prices[right] - prices[left]
                print('selling at ', prices[right])
                maxprofit = max(maxprofit, currprofit)
                right += 1

        return maxprofit



        