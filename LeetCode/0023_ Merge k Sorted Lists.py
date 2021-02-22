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