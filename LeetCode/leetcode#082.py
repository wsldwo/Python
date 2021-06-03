# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
    执行结果：通过
    执行用时：36 ms, 在所有 Python3 提交中击败了99.04%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了75.49%的用户
    一次通过Nice!!!这种题还是得好好画图，看清楚各种特殊情况。
    '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #链表为空，直接返回
        if not head:return
        #链表长为1，直接返回链表
        if not head.next:return head
        #添加Dummy节点，方便处理从头开始重复的链表
        dummy = ListNode('dummy',head)
        '''
        三指针
        l:重复开始节点的前驱节点
        m:重复开始节点
        r:重复结束节点
        '''
        l,m,r = dummy,head,head.next
        while r:
            #重复区间
            if m.val == r.val:
                while r and r.val == m.val:
                    r = r.next
                if r:
                    l.next = r
                    if r.next and r.val != r.next.val:
                        l = r
                        m = r.next
                        r = r.next.next
                    else:#此处l指针不能动
                        m = r
                        r = r.next
                else:
                    l.next = None
            #m、r不重复
            else:#全部向后移动一位
                l = l.next
                m = m.next
                r = r.next

        return dummy.next 
    '''
    执行结果：通过
    执行用时：48 ms, 在所有 Python3 提交中击败了67.08%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了46.16%的用户
    尝试代码简化,三指针降为双指针,令人惊讶的是时间还变长了！！！
    '''
    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head
        dummy = ListNode('dummy',head)
        # slow为重复节点的前驱节点 quick为重复节点的结束节点
        slow,quick = dummy,head
        while quick:
            #重复啦，重复啦！！
            if quick.next and quick.val == quick.next.val:
                dup = quick.val
                while quick and quick.val == dup:
                    quick = quick.next
                if quick:
                    slow.next = quick
                    if quick.next and quick.next.val != quick.val:
                        slow = quick
                        quick = quick.next
                else:
                    slow.next = None
            #不重复
            else:#都向后挪一位
                slow = slow.next
                quick = quick.next
        return dummy.next
