'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
n(nlogn) 알고리즘 Merge-Sort 활용
'''


class Solution:
    def sortList(self, head: ListNode) -> ListNode:  # 나누기
        if not head or not head.next:
            return head
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(start)

        return self.merge(l, r)

    def merge(self, l, r):  # 합치기
        if not l or not r:
            return l or r

        new_head = current = ListNode(0)
        while l and r:
            if l.val < r.val:
                current.next = l
                l = l.next
            else:
                current.next = r
                r = r.next
            current = current.next
        current.next = l or r

        return new_head.next