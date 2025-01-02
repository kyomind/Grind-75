# 找到起始點之後，立刻開始進行 連續序列 的迭代與確認，是比較有效的。
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest_streak = 0
        for num in num_set:
            # 只尋找 streak 的起點，其餘的數字都會被跳過
            if num - 1 not in num_set:
                # 沒有比 num 小 1 的數字，num 才能是 streak 的起點
                # 找到 streak 的起點，直開始計算 streak 的長度
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                # while 迴圈結束，current_streak 就是當前起始點的 streak 的長度

                longest_streak = max(longest_streak, current_streak)
                # 這裡也可以寫成
                # if current_streak > longest_streak:
                #     longest_streak = current_streak
        return longest_streak
