# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 使用雙指針(指針是抽象的，不是真正的指針，而且這裡只是原型)
# 2024-11-28 這個方法基本上就是迭代法
class Solution1:
    def mergeTwoLists(self, list1, list2):
        # 本題有一個要重新理解的地方就是雖然叫 list 不過當前總是只有一個節點
        # 所以實際上代表的是節點，而不是真正的 Python list
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


# 2024-11-28
# 自行實作迭代法
class Solution:
    def mergeTwoLists(self, list1, list2):
        # 先初始化答案容器，注意他可不是真正的list
        dummy = ListNode()
        list3 = (
            dummy  # XXX 這裡非常關鍵，兩者都是先指向同一個節點，所以之後list3的操作會影響到dummy
        )

        # 怎麼迭代這兩個「串列」就卡關了，想 for 就錯了，要用 while
        while list1 and list2:
            # if list1 <= list2: FIXME 錯誤的寫法！
            if list1.val <= list2.val:
                list3.next = list1  # XXX 這一步操作會影響到 dummy
                list1 = list1.next
            # list2 比較小
            else:
                list3.next = list2  # XXX 這一步操作會影響到 dummy
                list2 = list2.next

            # FIXME 忘記更新 list3(current)
            # 注意要在迴圈的範圍內更新
            list3 = list3.next  # XXX list3 重新指向新節點，所以之後的操作不會影響到 dummy

        # 只要有一個迭代結束，就會出回圈了，這個時候要檢查另外一個剩下多少
        # 然後把結果「接」上去
        if list1:
            list3.next = list1
        else:
            list3.next = list2

        # 去掉頭節點(虛擬)
        return dummy.next
