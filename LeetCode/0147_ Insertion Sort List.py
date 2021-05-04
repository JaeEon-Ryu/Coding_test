'''
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm.
The partially sorted list (black) initially contains only the first element in the list.
One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
현재 진행중인 노드 값을 이전 모든 값과 비교
while 전체노드 탐색
    while 이전 노드 값 비교
    값 비교 후 링크 끊고 이어주기
'''
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        added_head = ListNode(-5001, head)
        prev, current = added_head, head

        while current:
            if current.next and current.val > current.next.val:
                while prev.next and current.next.val > prev.next.val:
                    prev = prev.next
                temp = prev.next
                prev.next = current.next
                current.next = current.next.next
                prev.next.next = temp
                prev = added_head
            else:
                current = current.next

        return added_head.next
