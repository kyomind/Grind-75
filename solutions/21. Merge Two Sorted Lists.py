# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 使用雙指針
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 本題有一個要重新理解的地方就是雖然叫 list 不過當前總是只有一個節點
        # 所以實際上代表的是節點，而不是真正的串列
        # 這是為什麼 while 迴圈中有 list1 = list1.next 這樣的操作
        # 這在一般的迴圈操作，可是大忌（迭代中同時修改迭代對象），但這裡是可以的

        # 合併後串列的虛擬頭節點
        merged_list = ListNode()

        # 指向合併後串列的當前節點，這也是一個移動指針(但不是處理串列的指針)
        # 重點是，指針都是「抽象的」——想像中的，更像是一種流程控制
        current = merged_list
        while list1 and list2:
            # "<="，這同時處理了如果兩者相等的情況——以 list1 為主
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 這裡是處理其中一個串列已經走完的情況
        if list1:
            current.next = list1
        else:
            current.next = list2

        # 注意，虛擬頭節點的下一個節點才是合併後的串列
        # 虛擬頭節點的值為 0，不是真正的串列節點
        return merged_list.next
