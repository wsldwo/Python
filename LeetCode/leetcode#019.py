'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

 

示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        length = 1
        p = head # 复制头部
        while p.next:
            p = p.next
            length += 1
        if length == n:#删除头节点的特殊情况
            return head.next
        count = length - n - 1
        p = head # 复制头部
        while count > 0:
            p = p.next
            count -= 1
        if p:
            p.next = p.next.next
        return head
    
    def removeNthFromEnd2(self,head,n):
        quick = head #快指针 复制头部
        slow = head #慢指针 复制头部
        length = 0
        while quick:
            quick = quick.next
            length += 1
            if n >= 0:
                n -= 1
            else:
                slow = slow.next
        if slow == head and n == 0:#删除头节点
            return head.next
        if slow == head and n == -1 and length == 2:#删除尾节点
            head.next = None
            return head
        if slow:
            slow.next = slow.next.next
        return head

'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''