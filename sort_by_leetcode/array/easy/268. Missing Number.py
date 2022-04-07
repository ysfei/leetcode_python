"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

#brute force, O(N)
class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i,num in enumerate(nums):
            if num != i:
                return num
        

"""利用求和公式求解, O(1)"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n+1) / 2 - sum(nums) #一个list求和很方便：sum(nums)
