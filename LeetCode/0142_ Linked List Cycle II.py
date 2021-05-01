'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node_1 = node_2 = head
        while node_2 and node_2.next:
            node_1 = node_1.next
            node_2 = node_2.next.next

            if node_1 == node_2:
                break
        else:
            return None

        while node_1 != head:
            head = head.next
            node_1 = node_1.next

        return head
