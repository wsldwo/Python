'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
示例 2：


输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
示例 3：

输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]
示例 4：

输入：head = [1], k = 1
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        data = self.transferToList(head)
        result = []
        if len(data) < k:
            return head
        for i in range(0,len(data),k):
            temp = data[i:i+k]
            if len(temp) == k:#修正 只有切片长度等于k时，才进行逆转
                temp.reverse()
            result += temp
        return self.transferToListNode(result)

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