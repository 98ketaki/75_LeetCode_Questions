#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
  
def maxProfit(self, prices):
  max1=0
  min1=float('inf')
  for p in prices:
    min1=min(min1, p)
    profit=p-min1
    max1=max(max1, profit)
  return max1

#Sample
print(maxProfit([7,1,5,3,6,4]))
