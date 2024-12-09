"""
不是hash table就是排序
先用hash table
"""


# hash table
class Solution1:
    def containsDuplicate(self, nums):
        counter = {}
        for i in nums:
            # 對耶，完全不用管值，只要 key 重複了就是有重複的元素
            if i in counter:
                return True

            # 賦值內容其實也沒差，只要 key 重複就是有重複的元素
            counter[i] = 1

        return False


# 犯規做法，直接使用 Python set 的特性
# 僅供參考，不建議這樣寫
# beat 99%
class Solution2:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


# 其實有兩種的融合，直接使用set來實作原來的hash table
# 這樣就不用考慮值的問題，更加簡潔
# 因為用了迴圈，所以還是沒有直接使用set快(beat 72%)
class Solution3:
    def containsDuplicate(self, nums):
        counter = set()
        for i in nums:
            if i in counter:
                return True

            counter.add(i)

        return False


# 2024-12-09
class Solution:
    def containsDuplicate(self, nums):
        counter = set()
        for i in nums:
            if i in counter:
                return True
            counter.add(i)

        return False
