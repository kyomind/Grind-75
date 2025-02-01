# by ChatGPT + 部分我的註解，第一次先看懂所有的寫法與思路，並透過註解筆記
# 這個比克勞德版的更加直觀、好理解
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            """
            expand_around_center中，直接使用了外部函式的s參數，並沒有將其作為自己的參數
            這是否符合最佳實踐？

            在本函式中，直接引用了外部函式的 s 參數，這種設計在 Python 中是可行的，因為：
            - XXX Python 會在外部函式尋找變數，這屬於「閉包」的一部分，函式內部可以訪問外部範疇的變數
            - 程式碼簡潔：少傳遞一個參數，程式碼看起來更簡潔
            """
            # 向外擴展直到「邊界超出」或「字元不相等」
            # XXX 注意，左指針是 >=0，但右指針是 < len(s)，因為 len(s)本身已經超過index range
            # 注意，這個時候index是在中間，要向「兩邊」擴散，和一般的左右指針移動方向「相反」！
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # 繼續向左移動(擴散)——直到超過邊界，即小於0
                right += 1

            # XXX 當擴展停止(離開迴圈)時，left 和 right 的位置已經「超出了有效回文範圍」
            # 這時候，s[left + 1 : right] 才是最後一次擴展成功的回文子字串
            # XXX right 在 Python 切片中本來就不包括，所以它不必再特地-1
            return s[left + 1 : right]  # 返回擴展後的回文子字串

        longest_palindrome = ""

        for i in range(len(s)):
            # 以單字元為中心擴展（處理奇數長度回文）
            odd_palindrome = expand_around_center(i, i)
            # 以相鄰兩字元為中心擴展（處理偶數長度回文）
            even_palindrome = expand_around_center(i, i + 1)

            # 更新目前找到的最長回文子字串
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome
