# ai 給的解法，使用sort方法，排序時間複雜度為 O(nlogn)
# 略顯取巧，而且這個效能不佳，只有超過 13% 的人
class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 這題的關鍵是，因為 major element 出現次數超過 n/2，所以排序後，中間的元素一定是 major element
        nums.sort()
        return nums[len(nums) // 2]


# 我來試試暴力法
# 超過 18% 的人，效能仍然不佳
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

            if counter[n] > len(nums) // 2:
                return n


# Boyer-Moore Voting Algorithm
