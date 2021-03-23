/*
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Note: There will be some test cases with a board or a word larger than constraints to test if your solution is using pruning.
*/

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {

    let passed = false;

    let canGo = function (x, y, visited) {
        return inRange(x, y) && visited[x][y] == false;
    }

    let inRange = function (x, y) {
        return (0 <= x && x < board.length) && (0 <= y && y < board[x].length);
    }

    let dfs = function (x, y, visited, idx) {
        if (idx >= word.length || passed) { // 단어를 모두 찾았다는 뜻
            passed = true;
            return;
        }

        let dx = [0, 1, 0, -1];
        let dy = [-1, 0, 1, 0];

        for (let d = 0; d < 4; d++) {
            let newX = x + dx[d];
            let newY = y + dy[d];

            if (canGo(newX, newY, visited)) {
                if (word[idx] == board[newX][newY]) {
                    let copiedVisited = visited.map(v => v.slice()); // visited 복사
                    copiedVisited[newX][newY] = true;
                    dfs(newX, newY, copiedVisited, idx + 1); // 백트래킹
                }
            }
        }

    }

    let wordSearched = function (x, y) {

        // visited 배열 작성
        let visited = [];
        for (let t = 0; t < board.length; t++) {
            let temp = [];

            for (let t = 0; t < board[0].length; t++) {
                temp.push(false);
            }
            visited.push(temp);
        }
        visited[x][y] = true;

        if (word.length > 1) {
            dfs(x, y, visited, 1);
            return passed;
        }

        return true;
    }

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[i].length; j++) {
            if (board[i][j] == word[0] && wordSearched(i, j)) {
                return true;
            }
        }
    }

    return false;
};
