# by ChatGPT
# 我只是適度加入、刪除註解
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # 初始化結果陣列，大小與 nums 相同，初始值皆為 1
        answer = [1] * len(nums)

        # **第一遍遍歷：計算前綴乘積**
        # XXX 前綴乘積的初始值為 1，表示在最左側沒有任何數值時的乘積
        prefix = 1
        for i in range(len(nums)):
            # XXX 將目前的前綴乘積存到 answer[i]
            # 這就是為何需要初始化 answer，且讓所有元素皆為 1
            answer[i] = prefix
            # 更新前綴乘積，將當前的 nums[i] 乘進去
            prefix *= nums[i]

        # **第二遍遍歷：計算後綴乘積**
        # 後綴乘積的初始值為 1，表示在最右側沒有任何數值時的乘積
        suffix = 1
        # XXX 怎麼從右到左遍歷？這是一個挑戰——range 的第三個參數設為 -1 即可
        for i in range(len(nums) - 1, -1, -1):  # 從右到左遍歷
            # 將目前的後綴乘積乘進 answer[i]
            answer[i] *= suffix
            # 更新後綴乘積，將當前的 nums[i] 乘進去
            suffix *= nums[i]

        return answer
