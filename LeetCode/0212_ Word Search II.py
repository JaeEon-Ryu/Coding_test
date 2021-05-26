'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.

The same letter cell may not be used more than once in a word.
'''

# reference : lime66
class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode())
        root.word = word


class Solution(object):
    def search(self, i, j, root, board, m, n, r):
        char = board[i][j]
        if not (char and char in root.children):
            return

        board[i][j], root = None, root.children[char]

        if root.word:
            r.append(root.word)
            root.word = None

        for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ii, jj = i + x, j + y
            if 0 <= ii < m and 0 <= jj < n:
                self.search(ii, jj, root, board, m, n, r)

        board[i][j] = char

    def findWords(self, board, words):
        if not board:
            return []

        tree = Trie()
        [tree.insert(word) for word in words]

        m, n, r = len(board), len(board[0]), []

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                self.search(i, j, tree.root, board, m, n, r)
        return r


''' 시간제한 초과
class Solution:
    import copy
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        self.board = board
        self.is_on_the_board = False
        self.visited = [
            [False for j in range(len(board[i]))]
            for i in range(len(board))
        ]

        for word in words:

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == word[0]:  # 단어의 첫글자가 있으면 탐색 시작
                        self.is_on_the_board = False  # 초기화
                        self.init_visited()  # 초기화
                        self.bfs(word[1:], i, j, self.visited) # bfs으로 단어 탐색
                        if self.is_on_the_board:
                            result.append(word)
                            break

                if self.is_on_the_board: # 초기화
                    self.is_on_the_board = False
                    break

        return result

    def bfs(self, word: str, x: int, y: int, visited: List[List[int]]):
        if self.is_on_the_board:
            return

        if not word:
            self.is_on_the_board = True
            return

        visited[x][y] = True
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            # 범위 안에 있고, 방문하지 않았고, 다음 단어가 맞다면 bfs수행
            if self.in_range(new_x, new_y) and not visited[new_x][new_y] and self.board[new_x][new_y] == word[0]:
                self.bfs(word[1:], new_x, new_y, copy.deepcopy(visited))

    def in_range(self, x, y):
        return 0 <= x < len(self.board) and 0 <= y < len(self.board[x])

    def init_visited(self):
        for i in range(len(self.visited)):
            for j in range(len(self.visited[i])):
                self.visited[i][j] = False
'''

