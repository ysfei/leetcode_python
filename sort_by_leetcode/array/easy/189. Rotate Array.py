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

#就是左边变成n-k+1到n，右边变成1到n-k. 
#注意slicing是左闭右开，同时index=position-1。所以写成nums[n-k:n]和nums[0:n-k].而0和n是起始index所以可以省略
#rule of thumb 1: 如果想要slice positions [a,b], 写成nums[a-1:b], 里面个数是b-a+1.如果a-1=0或b=N可以省略，其中N是指len(nums)
#rule of thumb 2: 反过来，code中的nums[a:b]指的是positions[a+1,b], 里面个数是b-a.如果a省略了说明a=0，那就是positions[1,b],如果b省略了说明b=N，那就是[a+1,N]
#注意nums[N]不存在，但是nums[N-1:N]就是最后一个元素nums[N-1]
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
