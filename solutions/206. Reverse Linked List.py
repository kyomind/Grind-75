# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 與 ChatGPT 討論後重新來過，先用較簡單的迭代法
class Solution3:
    def reverseList(self, head):
        # 說真的，沒有這些自己的註解筆記，我很難看懂這段程式碼(一開始)
        prev = None
        current = head
        next_ = None
        while current:
            # 先取得下一個節點，存起來
            # 因為接下來會改變當前節點的指針，就再也找不到下一個節點了
            # next 是內建函式，所以用 next_ 來取代
            next_ = current.next

            current.next = prev  # XXX 這裡是關鍵，把當前節點的指針反轉
            prev = current  # 讓「上一個節點」更新為當前節點

            # 往下一個節點走，其實就是 current = current.next
            current = next_

        # 結束時，prev 就是反轉後的串列的頭節點(當前節點)
        return prev


# 2024-12-07
class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        next_ = None
        # while head 也不是不行，因為後不會再用到了
        # 只是操作過程中，head 這變數名稱具有誤導性
        while current:
            # 下一個節點先存起來，不然之後就訪問不到了
            next_ = current.next
            current.next = prev
            prev = current
            current = next_

        return prev
