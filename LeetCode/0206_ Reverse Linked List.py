'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
값을 갱신할 때마다 저장 위치를 tail쪽으로 이동시키는 방식
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        while head:
            new_head.val = head.val
            head = head.next
            new_head = ListNode(0,new_head)
        return new_head.next