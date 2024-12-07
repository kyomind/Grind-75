# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 直覺上答案是從最後拼回來，能做到嗎？難怪要用遞迴
# 看似簡單、直覺，但好像沒有那麼容易
# 直觀做法，但失敗: Memory Limit Exceeded
"""
ChatGPT 建議
在你的原始程式碼中，有兩個主要問題：

陣列存儲節點後指針方向未完全重新設置：在反轉鏈結串列時，應當斷開每個節點的原始指向，確保每個節點指向反轉過程中的新方向。
錯誤的虛擬頭節點操作：最終返回 reversed_head.next 可能無法指向正確的反轉後的起點。
"""


# 錯誤
class Solution1:
    def reverseList(self, head):
        nodes = []
        # 虛擬頭節點，不是答案的一部分
        reversed_head = ListNode()

        # XXX 注意，linked list 無法用 for in 來遍歷，所以只能用 while
        # 這裡的 head 是一個指針，不是真正的串列
        while head:
            nodes.append(head)
            head = head.next

        for i in reversed(nodes):
            reversed_head.next = i
            reversed_head = reversed_head.next

        return reversed_head.next


# 正確的做法(不考慮記憶體限制)
class Solution2:
    def reverseList(self, head):
        # 1. 用陣列存儲所有節點的引用
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        # 2. 反轉陣列中的節點指向
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]  # 每個節點指向前一個節點
        if nodes:
            nodes[0].next = None  # 最後一個節點指向 None

        # 3. 返回反轉後的頭節點
        return nodes[-1] if nodes else None


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


# 下次優先徒手做出迴圈法就好，這就是標準操作，解法都一樣
