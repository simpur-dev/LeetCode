# https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i/?envType=daily-question&envId=2026-02-08

from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1 = min2 = float('inf')  # 初始化：min1=全局最小值, min2=次小值
        for num in nums[1:]:         # 遍历除首元素外的所有元素（候选起始点）
            if num < min1:           # 情况1：发现新最小值
                min2 = min1          # 原最小值降级为次小值
                min1 = num           # 更新最小值
            elif num < min2:         # 情况2：介于 min1 和 min2 之间（含等于 min1 但小于当前 min2）
                min2 = num           # 更新次小值
        return nums[0] + min1 + min2 # 固定首元素 + 两个最小候选值