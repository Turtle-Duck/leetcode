# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    class ListNode():
        def __init__(self, x):
            self.val = x
            self.next = None

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rst = ListNode(0)
        start = rst
        jinwei = False
        while True:
            if l1 is None or l2 is None:
                break
            temp = l1.val + l2.val
            if jinwei:
                temp += 1
                jinwei = False
            if temp > 9:
                temp = temp - 10
                jinwei = True
            rst.val = temp
            rst.next = ListNode(0)
            rst = rst.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            if jinwei:
                temp = l1.val + 1
                jinwei = False
            else:
                temp = l1.val
            if temp > 9:
                temp = temp - 10
                jinwei = True
            rst.val = temp
            rst.next = ListNode(0)
            rst = rst.next
            l1 = l1.next

        while l2 is not None:
            if jinwei:
                temp = l2.val + 1
                jinwei = False
            else:
                temp = l2.val
            if temp > 9:
                temp = temp - 10
                jinwei = True
            rst.val = temp
            rst.next = ListNode(0)
            rst = rst.next
            l2 = l2.next

        if jinwei:
            rst.val = 1

        f = start
        s = f.next
        if s is not None:
            while s.next is not None:
                f = f.next
                s = s.next
            if s.val == 0:
                f.next = None

        return start


class Solution_good:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
