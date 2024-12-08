# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# + 2024-12-08
class Solution:
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 快慢指針，快指針一次走兩步，慢指針一次走一步
        # 當快指針走到結尾時，慢指針剛好走到中間
        slow = fast = head

        # XXX 依題目限制，節點最少有一個，所以不用檢查 head 是否為 None
        # 當節點只有一個時，直接回傳頭節點(此時中間節點就是頭節點)
        # 不會進入迴圈(XXX 因為此時 fast.next 會是 None)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
