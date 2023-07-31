def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    n = len(prices)
    max_list = [0]*n
    min_list = []
    max_val = 0
    min_val = prices[0]
    for i in range(n-1,-1,-1):
        max_val = max(max_val,prices[i])
        min_val = min(min_val,prices[n-i-1])
        max_list[i] = max_val 
        min_list.append(min_val) 

    ans = 0
    for i in range(n):
        ans = max(ans,max_list[i]-min_list[i])

    return ans


