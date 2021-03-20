/*
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
*/

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {

    let in_range = function (x, y) {
        return (0 <= x && x < matrix.length) && (0 <= y && y < matrix[0].length);
    }

    let initializeToZero = function (x, y) {
        let dx = [0, 0, 1, -1];
        let dy = [1, -1, 0, 0];

        for (let i = 0; i < 4; i++) {
            let new_x = x + dx[i];
            let new_y = y + dy[i];

            while (in_range(new_x, new_y)) {
                matrix[new_x][new_y] = 0;
                new_x += dx[i];
                new_y += dy[i];
            }
        }
    }

    let zeroPosition = [];
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            if (matrix[i][j] == 0) {
                zeroPosition.push([i, j]);
            }
        }
    }

    for (let pos of zeroPosition) {
        initializeToZero(pos[0], pos[1]);
    }

};


// 숫자 0 기준 해당 행,열 인덱스에 있는 모든 것들을 0으로 바꾸는 것이므로 
// 위처럼 함수를 만들지 않아도 된다. 
