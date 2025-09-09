# 1493 删掉一个元素以后全为 1 的最长子数组
'''
给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。
'''
class Solution:
    def longestSubarray(self, nums) :
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + 1 if nums[i] else 0
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] + 1 if nums[i] else 0

        ans = 0
        for i in range(n):
            pre_sum = pre[i - 1] if i > 0 else 0
            suf_sum = suf[i + 1] if i < n - 1 else 0
            ans = max(ans, pre_sum + suf_sum)

        return ans
nums = [1,1,0,1]
Solution().longestSubarray(nums)