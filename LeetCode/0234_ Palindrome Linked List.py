'''
Given the head of a singly linked list, return true if it is a palindrome.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head

        # slow 1개 증가 fast 2개 증가시킴으로써 중간지점 찾기
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 중간지점을 기점으로 order 이라는 리스트에 숫자들 추가
        order = []
        while slow:
            order.append(slow.val)
            slow = slow.next

        # 원본 head를 역순으로 정렬된 order과 비교
        for num in order[::-1]:
            if head.val != num:
                return False
            head = head.next

        return True