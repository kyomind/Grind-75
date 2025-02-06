# 不可以遍歷，因為這樣的時間複雜度是O(n)，不符合題目要求
# You must write an algorithm with O(log n) runtime complexity.
class Solution1:
    def search(self, nums, target):
        # 不可遍歷，只能透過 index 來找到 target
        left = 0
        right = len(nums) - 1

        # 最多執行 len(nums) 次，但這裡不可能達到最大次數
        # 也可以用 while left <= right: 來寫
        # XXX 2024-12-01 直接不管雙閉區間的 while 條件，狂了
        for _ in nums:
            # index 只能是整數，所以要用 // 來取整數
            # mid 是下一次的調整範圍邊界 index，取中間值
            # XXX 這個邊界值取到中間的偏左或右，都沒關係，因為接下來還會再比對範圍
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


# 2024-12-01
# 使用雙閉區間、while 迴圈
class Solution2:
    def search(self, nums, target):
        right = len(nums) - 1
        left = 0
        while right >= left:
            mid = (right + left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            # XXX 不能直接else，因為目標可能「不存在」
            elif nums[mid] == target:
                return mid
        return -1


# 2025-02-06 一樣，while、雙閉
# 手寫錯誤超多，還是不少細節
class Solution3:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        # mid = (left + right) // 2  XXX 位置錯誤，如此一來mid不會變動，因為下面內容完全沒有重設值的地方
        while right >= left:
            mid = (left + right) // 2

            # if mid == target:  XXX 不是比較index啦
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                # mid = right - 1   XXX 這裡很明顯寫錯了，範圍只縮小一點點，而不是減半
                # XXX mid 已經檢查過，不是target，因為是閉區間所以要right不能直接換成mid，而是要-1
                right = mid - 1
            elif nums[mid] < target:
                # mid = left + 1   XXX same
                left = mid + 1
        return -1
