class ListNode:#单链表
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        int1 = 0
        int2 = 0
        i = 0
        while l1:
            int1 += l1.val * (10**i)
            i += 1
            l1 = l1.next
        j = 0
        while l2:
            int2 += l2.val * (10**j)
            j += 1
            l2 = l2.next
        #print(int1,int2,int1+int2)
        result = int1 + int2
        root = None
        current_node = None
        #print('1',1,'#')
        #rint(root.val)
        for x in reversed(str(result)):
            if not root:
                root = ListNode(int(x))
                current_node = root
            else:
                current_node.next = ListNode(int(x))
                current_node = current_node.next
        print(root.val)
        self.printnode(root)
        return root
        '''
        #列表形式
        for i,x in enumerate(l1):
            int1 += x * (10**i)#10的i次幂
        for j,y in enumerate(l2):
            int2 += y * (10**j)#10的j次幂
        result = int1 + int2
        l_res = list(str(result))#整形转字符
        l_result = []
        for x in reversed(l_res):#逆转列表
            l_result.append(int(x))#字符转整形
        print(l_result)
        return l_result
        '''
    def printnode(self,node):
        l = []
        while node:
            l.append(node.val)
            node = node.next
        print(l)
node1 = ListNode(4)
node2 = ListNode(6)
node3 = ListNode(8)
node4 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4

node5 = ListNode(5)
node6 = ListNode(7)
node7 = ListNode(1)
node8 = ListNode(2)
node5.next = node6
node6.next = node7
node7.next = node8

s = Solution()
s.addTwoNumbers(node1,node5)