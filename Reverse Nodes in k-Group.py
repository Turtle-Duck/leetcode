#
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p_head = ListNode(0)
        p_head.next = head
        temp_head = p_head

        while True:
            Done = False
            tt_head = temp_head
            for i in range(k):
                if tt_head.next:
                    tt_head = tt_head.next
                else:
                    Done = True
                    break
            if Done:
                break

            new_end = temp_head.next

            father = temp_head.next
            son = temp_head.next.next
            for i in range(k - 1):
                # father = tt_head.next
                # son = tt_head.next.next
                new_son = son.next
                son.next = father
                father = son
                son = new_son

            temp_head.next = father
            new_end.next = son
            temp_head = new_end

        return p_head.next


if __name__ == '__main__':
    a = Solution()
    p = ListNode(1)
    p.next = ListNode(2)
    p.next.next = ListNode(3)
    p.next.next.next = ListNode(4)
    p.next.next.next.next = ListNode(5)
    rst = a.reverseKGroup(p, 3)
    print(rst)
