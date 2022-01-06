"""
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

 

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

 

提示：

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

 

进阶：

    尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
    你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lennums = len(nums)

        # 1
        # for i in range(k):
        # nums[:] = nums[lennums - 1 :] + nums[: lennums - 1]
        
        # 2
        # k = k % lennums
        # nums[:] = nums[lennums - k :] + nums[: lennums - k]

        # 3
        k %= lennums
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


list1 = [1, 2, 3, 4, 5, 6, 7]
S = Solution()
S.rotate(list1, 3)
print(list1)
