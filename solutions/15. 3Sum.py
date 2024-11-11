# 套路：先排序，然後使用雙指針
# Time: O(n^2)

# 「去除重複」是這題的一大難點，因為我們要找到所有不重複的三元組
# 所以我們需要在遍歷過程中去除重複的情況
# 解法 by ChatGPT
# XXX 本題無法使用 enumerate，因為需要同時使用 i, left, right 三個指針
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 初始化結果集
        result = []

        # XXX 排序是 3Sum 解法的核心前置步驟
        # 將 nums 進行排序，這樣可以方便我們進行雙指針操作和去重處理
        # 如果不可以用內建的sort方法，那就得自己實現排序
        nums.sort()

        # 遍歷 nums，每次固定一個數字 nums[i] 作為三元組的第一個數
        # -2 是因為至少要有三個數字，所以 i 最多到倒數第三個
        for i in range(len(nums) - 2):
            # 如果 i 大於 0，且當前數字與前一個數字相同，則跳過以避免重複
            # 這個判斷式在第一次遍歷時不會執行，因為 i = 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 初始化左右指針
            left, right = i + 1, len(nums) - 1

            # 開始雙指針搜尋，找到和為 0 的組合
            # XXX 一前一後，從兩側逐步逼近，在兩者相遇時，結束迴圈
            while left < right:
                # 計算三個數的和
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    # 如果和小於 0，說明需要更大的數字，因此左指針右移
                    left += 1

                elif total > 0:
                    # 如果和大於 0，說明需要更小的數字，因此右指針左移
                    right -= 1

                else:
                    # 如果和為 0，找到符合條件的三元組，將其加入結果集中
                    # XXX 但還沒完！因為後續還可能有其他符合條件的三元組
                    result.append([nums[i], nums[left], nums[right]])

                    # 移動左指針，跳過重複的數字，以避免同一組三元組出現重複
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # 移動右指針，跳過重複的數字，以避免同一組三元組出現重複
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 移動左右指針到下一個位置，尋找下一組可能的三元組
                    left += 1
                    right -= 1

        # 返回所有符合條件的三元組
        return result
