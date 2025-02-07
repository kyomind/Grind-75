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
            # 2025-02-07 其實你可以用 if/else 就沒這問題了
            # hash_map[n] = i XXX 位置錯誤
            # XXX 這行是最重要的，完全解釋了為何 key 是值而不是索引
            if target - n in hash_map:
                # return [hash_map[n], i]  # XXX 錯誤了
                return [hash_map[target - n], i]

            hash_map[n] = i


"""
一個簡單的道理就是你把 If/Else 改成 衛語句 的時候 If 一定是先的
所以 hash_map[n] = i 不可以放在 if 之前
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index_mapping = {}
        for i in range(len(nums)):
            # target - nums[i]，就是key
            # another_num = target - nums[i]
            # if another_num in num_to_index_mapping:
            if target - nums[i] in num_to_index_mapping:
                # 這裡只是使用同一個 key 去取值而已！完全沒變
                # return [i, num_to_index_mapping[another_num]]
                return [i, num_to_index_mapping[target - nums[i]]]

            else:
                num_to_index_mapping[nums[i]] = i
