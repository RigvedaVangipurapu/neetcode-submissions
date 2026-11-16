class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float("inf")] * n
        print(prices)
        prices[src] = 0

        for i in range(k+1):
            temp_price = prices.copy()

            for s , d, p in flights:
                # print("checking ",s,d,p)
                if prices[s] == float("inf"):
                    pass
                
                #relax the edges
                temp_price[d] = min(prices[s] + p , temp_price[d])

            prices = temp_price.copy()

        return -1 if prices[dst] == float('inf') else prices[dst]






      
        