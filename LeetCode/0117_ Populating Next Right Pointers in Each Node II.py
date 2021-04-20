'''
Given a binary tree

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
전위순회를 활용하여 노드들을 탐색함
노드들을 탐색할 때마다 각 레벨에 해당하는 root값을 저장하도록 함
( 레벨에 해당하는 root가 이미 존재한다면 해당 root를 pop하고 next 정보를 기록 후 갱신함)
'''


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        self.nodes = []
        self.preorder_search(root, 1)

        return root

    def preorder_search(self, root: 'Node', level: int):
        if len(self.nodes) < level:
            self.nodes.append(root)
        else:
            same_level = self.nodes.pop(level - 1)
            same_level.next = root
            self.nodes.insert(level - 1, root)

        if root.left:
            self.preorder_search(root.left, level + 1)
        if root.right:
            self.preorder_search(root.right, level + 1)