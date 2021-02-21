# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # Convert to List
        li = []
        while head != None:
            li.append(head.val)
            head = head.next

        # Remove Nth Node From End of List
        del li[len(li) - n]

        # Convert to singly_linked list
        result = ListNode('')
        if li:
            result.val = li[0]
            curr_node = result

            for i in range(1, len(li)):
                curr_node.next = ListNode(li[i])
                curr_node = curr_node.next

        return result



'''
someone else's solution
reference : StefanPochmann
class Solution:
    def removeNthFromEnd(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next
'''