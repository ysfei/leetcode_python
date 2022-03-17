"""

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""
"""使用53题的思路，两个变量"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curSum=maxSum=0 #可以连等，不错！
        for i in range(1,len(prices)):
            curSum=max(0,curSum+prices[i]-prices[i-1]) 
    #开始的条件是当前price比上一个起始点更低，即从上一个起始点开始累计的return<0，此时重新开始累计
            maxSum = max(curSum,maxSum)
    #结束的条件是当前的累计return比储存的所有累计return都要高
        return maxSum
    #这一类题目（对一个动作的起始点都要做决定）都可以通过在每个点做决定的方法来减少时间复杂度：每个点决定要不要开始/结束
    #节省时间复杂度，暴力解法是对起始点各做循环，复杂度O(n^2)。现在复杂度是O(n)
