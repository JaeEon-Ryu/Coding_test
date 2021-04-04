'''
Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
'''

'''
트리의 왼쪽 하위 노드는 루트보다 작다
트리의 오른쪽 하위 노드는 루트보다 크다
'''
class Solution:

    # reference : jose14520

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.generator(1, n)

    def generator(self, start, end):
        if start > end:  # edge case, see exposition below
            return [None]

        all_trees = []  # list of all unique BSTs
        for current_root in range(start, end + 1):  # generate all roots using list [start, end]
            # recursively get list of subtrees less than curRoot
            all_left_subtrees = self.generator(start, current_root - 1)

            # recursively get list of subtrees greater than curRoot
            all_right_subtrees = self.generator(current_root + 1, end)

            for left_subtree in all_left_subtrees:  # get each possible left subtree
                for right_subtree in all_right_subtrees:  # get each possible right subtree
                    # create root node with each combination of left and right subtrees
                    curRoot = TreeNode(current_root)
                    curRoot.left = left_subtree
                    curRoot.right = right_subtree

                    # curRoot is now the root of a BST
                    all_trees.append(curRoot)

        return all_trees