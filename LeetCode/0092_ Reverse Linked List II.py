'''
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        result = ListNode()
        res_temp = result
        mid = []
        idx = 1

        while head:
            if not (left <= idx <= right):
                res_temp.next = ListNode(head.val)
                res_temp = res_temp.next
            else:  # 반대로 뒤집을 값들
                mid.append(head.val)
                if idx == right:
                    while mid:
                        res_temp.next = ListNode(mid.pop())
                        res_temp = res_temp.next

            head = head.next
            idx += 1

        return result.next