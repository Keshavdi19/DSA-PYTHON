def profit(prices):
    n = len(prices)
    max_profit = 0
    for i in range(0,n):
        for j in range(i+1, n):
            if prices[j] > prices[i]:
                p = prices[j] - prices[i]
                max_profit = max(max_profit,p)
    return max_profit
print(profit([7,2,1,5,6,4,8]))
# optimal approach
def maxprofit(price):
    n = len(price)
    max_profit = 0
    min_price = float("inf")
    for i in range(0, n):
        min_price = min(min_price, price[i])
        max_profit = max(max_profit,price[i] - min_price)
    return max_profit
print(maxprofit([7,2,1,5,6,4,8]))

