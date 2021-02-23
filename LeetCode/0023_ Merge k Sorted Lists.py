# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        result = curr_node = ListNode(0)
        unsorted_list = []

        for list in lists:
            while list:
                unsorted_list.append(list.val)
                list = list.next

        for num in sorted(unsorted_list):
            print(curr_node)
            curr_node.next = ListNode(num)
            curr_node = curr_node.next

        return result.next


'''
cbmbbz's solution - using priority queue

from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next

'''