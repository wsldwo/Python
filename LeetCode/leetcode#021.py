'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = self.transferToList(l1)
        list2 = self.transferToList(l2)
        list3 = list1 + list2
        list3.sort()
        print(list3)
        return self.transferToListNode(list3)

    def transferToList(self,ln):
        l = []
        while ln:
            l.append(ln.val)
            ln = ln.next
        return l

    def transferToListNode(self,l):
        ln = ListNode()
        p = ln # 复制头节点
        for x in l:
            p.next = ListNode(val=x)
            p = p.next
        return ln.next
            

s = Solution()
s.mergeTwoLists(None,ListNode(0))
    