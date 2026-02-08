# https://leetcode.cn/problems/find-smallest-letter-greater-than-target/?envType=daily-question&envId=2026-02-08

import bisect
#题目中，letters 是一个非递减排序的字符列表，此时可以考虑二分查找，找到第一个大于 target 的字符
#import bisect是Python标准库中的一个模块，用于二分查找。
from typing import List
#python<3.9时，只能用List[str]，不能用list[str]，如果用了List[str]，则必须有from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        #bisect.bisect_right(letters, target)返回的是letters中第一个大于target的元素的索引
        #如果target大于letters中的所有元素，则返回len(letters)
        idx = bisect.bisect_right(letters, target)

        return letters[0] if idx == len(letters) else letters[idx]