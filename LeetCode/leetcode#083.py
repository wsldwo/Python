class Solution:
    '''
    执行结果：通过
    执行用时：56 ms, 在所有 Python3 提交中击败了20.24%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了53.66%的用户
    力扣这耗时是不是乱填的啊！！！
    '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #此题可以不创建Dummy节点，因为首节点不必删除
        #仍然使用快慢指针
        if not head or not head.next:
            return head
        # slow为重复区间的起始节点 quick为重复区间的结束节点
        slow,quick = head,head.next
        while quick:
            if slow.val == quick.val:#前后重复
                while quick and quick.val == slow.val:
                    quick = quick.next
                if quick:
                    slow.next = quick #进行连接
                    slow = quick
                    quick = quick.next
                else:
                    slow.next = None
            else: #前后不重复，都向后挪一位
                slow = slow.next
                quick = quick.next
        return head
    
    '''
    试试评论区看到的递归套路
    执行结果：通过
    执行用时：56 ms, 在所有 Python3 提交中击败了20.24%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.17%的用户
    结果跟上边速度差不多
    '''
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def delete(head):
            if not head or not head.next:
                return head
            if head.val == head.next.val:
                #删除当前节点，即对head重新赋值
                head = delete(head.next)
            else:
                #保留当前节点，即对head.next重新赋值
                head.next = delete(head.next)
            return head
        return delete(head)

