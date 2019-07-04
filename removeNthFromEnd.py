# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = head
        for i in range(n):
            p1 = p1.next
        if not p1:
            return head.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        if p2.next is not None:
            p2.next = p2.next.next
        else:
            head = None
        return head