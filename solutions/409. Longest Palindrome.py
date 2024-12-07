# 感覺本題就是有點索然無味
# 沒有什麼技巧，就是純粹的統計字母出現的次數，然後計算最長的回文長度
"""
爭點：
- 字典統計，但不用管具體有哪些鍵(重要)，只要迴圈處理、加總
- 透過判斷式區分偶數與奇數值的值，以組成最大長度
- 判斷式的應用——只能加一次奇數
"""


class Solution1:
    def longestPalindrome(self, s: str):
        # 用字典統計每個字母出現的次數
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        longest_length = 0  # 初始化最長回文長度
        for c in count:
            # 確保只會加偶數次
            # ex: 3 // 2 * 2 = 2
            # ex: 4 // 2 * 2 = 4
            # ex: 5 // 2 * 2 = 4
            # ex: 6 // 2 * 2 = 6
            longest_length += count[c] // 2 * 2

            # 只會加一次，因為如果長度變成奇數(加過了)，就不會再加了
            if longest_length % 2 == 0 and count[c] % 2 == 1:
                longest_length += 1

        return longest_length


# 2024-12-07
class Solution:
    def longestPalindrome(self, s: str):
        counts = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1

        longest_count = 0
        has_odd = False
        for count in counts.values():
            if count % 2 == 0:
                longest_count += count
            else:
                longest_count += count - 1
                has_odd = True

        return longest_count + has_odd  # 利用 bool 也是 int 的特性
