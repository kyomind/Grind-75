class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 忘記把字典初始化放在迴圈外，我無言
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], i]
            hash_map[num] = i


# 2024-11-23
class Solution2:
    def twoSum(self, nums, target):
        hash_map = {}
        for i, n in enumerate(nums):
            # 為何這裡只是提前，就無法通過了？詳見Markdown
            hash_map[n] = i
            # XXX 這行是最重要的，完全解釋了為何 key 是值而不是索引
            if target - n in hash_map:
                return [hash_map[n], i]
