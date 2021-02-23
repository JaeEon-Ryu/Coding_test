# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        result = curr_node = ListNode(0)

        nums = []

        while head:
            nums.append(head.val)

            if len(nums) == k:
                for _ in range(k):
                    curr_node.next = ListNode(nums.pop())
                    curr_node = curr_node.next

            head = head.next

        if nums:
            for idx in range(len(nums)):
                curr_node.next = ListNode(nums[idx])
                curr_node = curr_node.next

        return result.next





