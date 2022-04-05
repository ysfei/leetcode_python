"""

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

"""

"""
暴力解法(n^2)：
class Solution(object):
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num
这里可以学习对list里出现某个值的计数方法：count = sum(1 for i in nums if i==target)
但这个解法暴力在sum(1 for ...)本身也是循环，所以复杂度是n^2.

巧思路（NlogN)
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        #或者直接一行：return sorted(nums)[len(nums)//2]
缺点是sort的时间复杂度是NlogN

Hash table解法(n):
from collections import Counter
class Solution:
    def majorityElement(self, nums):
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)
这里import了Counter函数，直接生成各个值的频度表，format是dictionary (Hash table)
max函数的key选项用于比大小的数字和return数字不同的情况，比如要比较x^2时就用 max(nums, key=lambda x: x**2)
counts.keys()表示要return的数字是ditionary keys种的一个（得有括号，否则只是个函数）。counts.get是个函数（没有括号），给出key对应的值
也可以把函数用lambda写出来 max(counts.keys(), key=lambda x:counts[x])
Counter和max都是n时间复杂度，所以总共时间复杂度也是n。

Boyer-Moore Voting Algorithm （n)
class Solution(object):
    def majorityElement(self, nums):
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate

