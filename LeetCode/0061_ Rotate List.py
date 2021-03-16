'''
Given the head of a linked list, rotate the list to the right by k places.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or head.next == None:
            return head

        def len_list():
            cur, cnt = head, 0
            while cur:
                cur = cur.next
                cnt += 1
            return cnt

        for _ in range(k % len_list()):
            temp = head
            tail = 0
            while True:
                if head.next.next != None:
                    head = head.next
                else:
                    tail = head.next
                    head.next = None
                    break

            tail.next = temp
            head = tail

        return head