'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

'''
왼쪽 자식이 있다면 - 오른쪽 자식과 이어주기
    같은 레벨에 노드가 존재한다면 (next가 있다면) - 왼쪽 노드의 오른쪽 자식과, 오른쪽 노드의 왼쪽 자식 이어주기
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        self.generator(root)
        return root

    def generator(self, root: 'Node'):
        if root.left:
            root.left.next = root.right

            if root.next:
                root.right.next = root.next.left

            self.generator(root.left)
            self.generator(root.right)