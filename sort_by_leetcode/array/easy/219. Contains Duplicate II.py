"""

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

"""
"""仍然用dict保存数组元素出现的位置，两种情况下更新"""
#和217一样，无非在判断num in dic时多加一个条件：index - dic[num] <= k，以及在dict中的value不能乱写了，得用nums的index
#for i in nums: 返回list values
#for i,value in enumerate(nums): 返回nums的 (index,value) pair
#for i in dic: 返回dictionary keys, 相当于for i in dic.keys()
#for i in dic.values(): 返回dictionary values
#for i,value in dic.items(): 返回dictionary的 (key,value) pair
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = dict()
        for index,value in enumerate(nums): 
            if value in dic and index - dic[value] <= k:
                return True
            dic[value] = index
        return False
