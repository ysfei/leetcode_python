"""

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Subscribe to see which companies asked this question.

"""
"""利用hash table，别忘了判断空数组的情况.其实更麻烦"""
#如果是暴力解法，会在loop over num的过程中再与过去的出现过的num进行比较，O(N^2).
#所以常用技巧就是把查找过去出现过的num的任务交给dict，num in dict的复杂度只O(1).所以总的复杂度只有O(N)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        dic = dict() #建立空dict的方法： dict()
        for num in nums:
            if num in dic:
                return True #一旦出现return，整个def直接结束（不只是loop结束）
            dic[num] = 1 #if num in dic的in函数判断的是keys而不是dic中的values，所以直接用当前num作为key，value就随便（比如1）
        return False

"""直接利用set的性质反而更简单"""
#set()提取nums中的distinct values生成一个set. 原因很简单：set这种data type不能包含重复元素
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
