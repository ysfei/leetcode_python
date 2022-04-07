"""

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

"""
"""直接拼接数组即可"""

#就是左边变成n-k+1到n，右边变成1到n-k. 注意slicing是左开右闭，所以写成nums[n-k:n]和nums[0:n-k].而0和n是起始index所以可以省略
#不知道为什么LHS写成nums[:]，直接用nums就可以了，别忘了还要写return nums
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[n - k:] + nums[:n - k]
