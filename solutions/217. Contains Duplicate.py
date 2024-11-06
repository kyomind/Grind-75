"""
不是hash table就是排序
先用hash table
"""


# hash table
class Solution1(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = {}
        for i in nums:
            # 對耶，完全不用管值，只要 key 重複了就是有重複的元素
            if i in counter:
                return True

            # 賦值內容其實也沒差，只要 key 重複就是有重複的元素
            counter[i] = 1

        return False


# 犯規做法，使用Python set
# 僅供參考，不建議這樣寫
# beat 99%
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
