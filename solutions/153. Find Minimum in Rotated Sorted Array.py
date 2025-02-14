class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        # # 搜尋範圍是 [left, right)，因此終止條件是 left == right
        while left < right:
            mid = (left + right) // 2

            # 答案在不正常有序的那側，即分界點
            if nums[mid] > nums[right]:
                # 右半邊不正常，答案在右半邊
                left = mid + 1

            else:
                # 答案在左半邊，且包括mid本身也可能是答案
                right = mid

        # 兩者最終會相遇，達成終止條件，脫離迴圈
        # 因為指針並不會跳著移動(+2/-2)，所以相遇時就會脫離迴圈，不可能發生 left > right 的情況
        return nums[left]
