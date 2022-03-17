"""

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

"""

"""其实跟第一题是一样的题目"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
#暴力解法是n^2的复杂度，这里无非是偷懒了，把第二层循环替换成找dictonary的key
#难点就在于dictionary的value是不能直接查找的，但我们把数值存在key里面就可以直接查找
"""
其实这个答案的写法已经很花哨了，最质朴的写法是：
        res = dict()
        for i in range(0,len(numbers)):
            res[numbers[i]] = i
        for i in range(0,len(numbers)):
            sub = target - numbers[i]
            if sub in res.keys():
                return [res[sub]+1,i+1]
给出的最优解无非是把两个相似的循环结合在一起，又省了一些iteration，不过复杂度of the same magnitude
"""              
        res = dict()
        for i in range(0,len(numbers)):
            sub = target - numbers[i]
            if sub in res.keys():
                return [res[sub]+1,i+1]
            else:
                res[numbers[i]] = i
        return []
