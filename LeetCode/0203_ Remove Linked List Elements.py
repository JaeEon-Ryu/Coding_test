'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.
val == val, and return the new head.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode()
        node = new_head
        while head:
            if head.val != val: # 주어진 val값이 아니라면 리스트노드 저장하기
                node.next = ListNode()
                node = node.next
                node.val = head.val
            head = head.next

        return new_head.next