'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    from collections import deque
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        info = deque()

        search = head
        while search:
            info.append(search.val)
            search = search.next

        modified = head
        for i in range(len(info)):
            if i % 2 == 0:
                modified.val = info.popleft()
            else:
                modified.val = info.pop()

            modified = modified.next



''' 노드의 값을 변경시키지 않고 해결하는 방법 ( reference : OldCodingFarmer )
def reorderList(self, head):
    if not head:
        return
    # ensure the first part has the same or one more node
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    p = slow.next
    slow.next = None
    node = None
    while p:
        nxt = p.next
        p.next = node
        node = p
        p = nxt
    # combine head part and node part
    p = head
    while node:
        tmp = node.next
        node.next = p.next
        p.next = node
        p = p.next.next #p = node.next
        node = tmp
'''