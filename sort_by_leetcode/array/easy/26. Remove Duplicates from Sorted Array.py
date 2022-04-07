"""

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question.

"""

"""题目要点：返回不重复数的个数，同时要排在数组的前面n个"""
#loop over i in range(len(nums))
#如果num[i]和第一个num相同就跳过，如果不同就留下replace第二个num (index=1, replacenums[1])，进入下一个i; 
#...
#如果num[i]和上一个num相同就跳过，如果不同就留下replace上一个num的后面那一个 (index=index+1并replace nums[index])，进入下一个i;
#因为i的增速>=index的增速，所以replace nums[index]不会影响之后对nums[i]的比较
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index = index + 1
                nums[index] = nums[i]

        return index + 1
