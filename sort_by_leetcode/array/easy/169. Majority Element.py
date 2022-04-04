"""

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

"""

"""思路，因为出现次数最多的元素大于元素个数的一半，所以使用count和cand，设目标值为a
"""

"""
暴力解法：
class Solution(object):
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num
这里可以学习对list里出现某个值的计数方法：count = sum(1 for i in nums if i==target)
但这个解法暴力在sum(1 for ...)本身也是循环，所以复杂度是n^2.
                
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                cand, count = i, 1
            else:
                if i == cand:
                    count = count + 1
                else:
                    count = count - 1
        return cand
"""一行的思路"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]
