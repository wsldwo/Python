# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    执行结果：通过
    执行用时：40 ms, 在所有 Python3 提交中击败了84.57%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了72.95%的用户
    Nice!!!一次通过！！
    '''
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        def length(head):
            ll,p,end = 0,head,None
            while p:
                if p.next == None:
                    end = p
                ll += 1
                p = p.next
            return ll,end
        
        r = length(head)
        list_len,end = r[0],r[1] #真正的尾节点
        k = k % list_len # 当逆转次数当好等于单链表长度时，链表又回到最初的样子，所以这里直接做模运算求出有效的逆转次数
        if k == 0:#可以整除
            return head#直接返回原链表
        '''
        使用双指针找到被挤出去那一段的  起点前驱  和  终点  ，交换前后两段
        '''
        slow,quick = head,head
        #快指针领先 k 个节点
        conut = 0
        while conut < k:
            quick = quick.next
            conut += 1
        while quick:
            if quick.next == None:
                #到达尾节点
                break
            else:
                quick = quick.next
                slow = slow.next
        
        newhead = slow.next
        slow.next = None
        quick.next = head
        return newhead
        
        
        
        

        
