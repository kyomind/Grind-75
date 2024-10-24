# 不可以遍歷，因為這樣的時間複雜度是O(n)，不符合題目要求
# You must write an algorithm with O(log n) runtime complexity.
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 不可遍歷，只能透過 index 來找到 target
        left = 0
        right = len(nums) - 1

        # 最多執行 len(nums) 次，但這裡不可能達到最大次數
        for _ in nums:
            # index 只能是整數，所以要用 // 來取整數
            # mid 是下一次的調整範圍邊界 index，取中間值
            # 這個邊界值取到中間的偏左或右，都沒關係，因為接下來還會再比對範圍
            mid = (left + right) // 2
            # 剛好找到 target
            if nums[mid] == target:
                return mid
            # 前面已經不等於了，所以這裡只會是大於或小於，不會有等於了
            # 我們選擇小於，那 else 就是大於的情況(反之亦然)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
