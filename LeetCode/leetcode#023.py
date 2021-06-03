'''
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        total_list = []
        for list in lists:
            total_list += self.transferToList(list)
        
        if len(total_list) == 0:
            return None
        
        print(total_list)
        total_list.sort()
        return self.transferToListNode(total_list)

    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = self.transferToList(l1)
        list2 = self.transferToList(l2)
        list3 = list1 + list2
        list3.sort()
        print(list3)
        return self.transferToListNode(list3)
    '''

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