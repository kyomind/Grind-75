# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 雙指針法
class Solution1:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 雙指針法: 快慢指針
        # 起點相同，快指針走兩步，慢指針走一步
        fast = slow = head

        # 當 head 不為 None 時，進入迴圈——XXX 無限迴圈
        # XXX 脫離迴圈的方式只有兩種：
        # 1. 快指針走到 linked list 的尾端
        # 2. 進入 cycle 且快慢指針相遇
        while head:
            # XXX 快指針經過的節點都不得為 None（這一步和下一步不得為 None）
            # 2024-12-04 真的很重要！
            if fast and fast.next:
                fast = fast.next.next
            # 快指針走到 None 時，代表已達 linked list 尾端，結束迴圈，無cycle
            else:
                return False

            # 慢指針只要一直往前走就好
            # 因為慢指針不會走到 None（有 None 的話，快指針會先走到）
            slow = slow.next

            # 如果快慢指針相遇，代表有cycle
            if fast is slow:
                return True

        # 當 head 為 None 時，為空的 linked list，不可能有 cycle
        return False


# hash table


# 2024-12-04
# 先用雙指針
class Solution:
    def hasCycle(self, head):
        if head is None:
            return False

        fast = slow = head
        # 如果用 head，可以直接省略上面的檢查，查優雅
        while True:
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
            else:
                # 快指針遇到none先結束，可確定沒有循環
                # XXX 因為有循環的話，無論快慢指針都「永遠不會結束」
                return False

            if slow is fast:
                # 只有一種情況為true，即兩個指針相遇
                return True
