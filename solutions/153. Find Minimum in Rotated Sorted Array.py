class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            # 答案在不正常有序的那側，即分界點
            if nums[mid] > nums[right]:
                # 右半邊不正常，答案在右半邊
                left = mid + 1

            else:
                # 答案在左半邊，且包括mid本身也可能是答案
                right = mid

        # 兩者最終會相遇，因為並不會跳著移動
        return nums[left]
