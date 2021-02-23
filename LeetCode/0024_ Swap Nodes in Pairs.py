# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        result = curr_node = ListNode(0)

        is_odd = True
        temp = 0

        while head:
            # Store values in temp when odd
            if is_odd:
                temp = head.val
                is_odd = False
            # Store the current value when even and store the value that was in temp
            else:
                curr_node.next = ListNode(head.val)
                curr_node = curr_node.next

                curr_node.next = ListNode(temp)
                curr_node = curr_node.next
                is_odd = True

            head = head.next

        # Save if temp has any remaining values
        if not is_odd:
            curr_node.next = ListNode(temp)

        return result.next