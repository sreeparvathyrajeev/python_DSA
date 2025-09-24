#brute force approach
# Python Program to solve stock buy and sell by  
# exploring all possible pairs

def max_profit(prices):
    n = len(prices)
    res = 0

    # Explore all possible ways to buy and sell stock
    for i in range(n - 1):
        for j in range(i + 1, n):
            res = max(res, prices[j] - prices[i])
    
    return res




#better approach

def max_profit2(prices):
    n=len(prices)
    min_price=prices[0]
    max_profit=0
    for i in range(1,n):
        min_price=min(min_price,prices[i])
        max_profit=max(max_profit,prices[i]-min_price)
    return max_profit




if __name__=="__main__":
    prices=str(input()).split()
    prices=[int(i) for i in prices]
    print(max_profit2(prices))
    

