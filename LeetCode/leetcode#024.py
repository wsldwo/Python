'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next == None:
            return head
        
        def swap(p0,p1,p2):#p0 前驱节点 p1 节点1 p2 节点2
            p1.next = p2.next
            p2.next = p1
            p0.next = p2
        
        dummy = ListNode(val='dummy',next=head) #添加dummy节点，方便处理头节点

        p0 = dummy
        p1 = head
        p2 = head.next

        while p2:
            swap(p0,p1,p2)

            #位置复原
            p3 = p2
            p2 = p1
            p1 = p3

            #前进两格
            if p2.next:
                if p2.next.next:
                    p0 = p0.next.next
                    p1 = p1.next.next
                    p2 = p2.next.next
                else:
                    return dummy.next
            else:
                return dummy.next
        
        return dummy.next

            

