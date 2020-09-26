'''
1. 이진 트리 초기화
2. 노드 삽입
(삽입 순서 - y축 내림차순 // root -> leaf )
3. 전위, 후위 재귀 구현
4. 만들어진 리스트로 인덱스 값 찾기
'''

import sys
sys.setrecursionlimit(10**6)

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
pre_list = []
post_list = []

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                pre_list.append(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)

        _pre_order_traversal(self.root)

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                post_list.append(root.data)

        _post_order_traversal(self.root)


def solution(nodeinfo):

    info_copy = sorted(nodeinfo,key=lambda x:x[1],reverse=True)
    bst = BinarySearchTree()

    for x in info_copy:
        bst.insert(x)

    bst.pre_order_traversal()
    bst.post_order_traversal()

    pre_answer = list()
    post_answer = list()

    for pre,post in zip(pre_list,post_list):
        pre_answer.append(nodeinfo.index(pre)+1)
        post_answer.append(nodeinfo.index(post)+1)

    return [pre_answer,post_answer]

print(solution(nodeinfo))

#array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
#array = [30,20,40,14,25,45,15,28,26]







