  #https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
  
  def maxProfit(self, prices):
    max1=0
    min1=float('inf')
    for p in prices:
      min1=min(min1, p)
      profit=p-min1
      max1=max(max1, profit)
    return max1
