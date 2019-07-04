# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def mergeKLists(self, lists):
        n = len(lists)
        if n == 0:
            return []
        rst = ListNode(0)
        head = rst
        while True:
            small = 1e30
            small_index = 0
            Down = True
            for i in range(n):
                if lists[i] and lists[i].val < small:
                    Down = False
                    small = lists[i].val
                    small_index = i
            if Down:
                break
            lists[small_index] = lists[small_index].next
            rst.next = ListNode(small)
            rst = rst.next
        return head.next