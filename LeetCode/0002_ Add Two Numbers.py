# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def from_list_to_reversed_num(li):

            str_li = ''
            while li != None:
                str_li += str(li.val)
                li = li.next

            return int(str_li[::-1])

        # the added_num before reverse ( int )
        added_num = from_list_to_reversed_num(l1) + from_list_to_reversed_num(l2)

        # the added_num after reverse ( str )
        added_num = str(added_num)[::-1]

        # make result to singly-linked list
        result = ListNode(int(added_num[0]))
        curr_node = result

        for i in range(1, len(added_num)):
            curr_node.next = ListNode(int(added_num[i]))
            curr_node = curr_node.next

        return result

