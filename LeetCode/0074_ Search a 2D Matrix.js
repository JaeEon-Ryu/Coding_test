/*
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
*/


/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {

    let binarySearch = function (val, position) {

        if (position == 'row') {
            let left = 0;
            let right = matrix.length - 1;
            let mid;

            while (left <= right) {
                mid = parseInt((left + right) / 2);

                if (matrix[mid][val] < target) {
                    left = mid + 1;
                }
                else if (matrix[mid][val] > target) {
                    right = mid - 1;
                }
                else {
                    return mid;
                }
            }

            return right;
        }
        else {
            let left = 0;
            let right = matrix[0].length - 1;
            let mid;

            while (left <= right) {
                mid = parseInt((left + right) / 2);

                if (matrix[val][mid] < target) {
                    left = mid + 1;
                }
                else if (matrix[val][mid] > target) {
                    right = mid - 1;
                }
                else {
                    return mid;
                }
            }

            return mid;
        }

    };

    // 예외처리 추가 ( 길이가 1이거나 2일경우 이진탐색 인덱스 오류 -> 수정 )

    // 행 인덱스 찾기
    let rowValue;
    rowValue = (matrix.length == 1) ? 0 : binarySearch(0, 'row');
    rowValue = rowValue < 0 ? 0 : rowValue;
    // 열 인덱스 찾기
    let columnValue;
    columnValue = (matrix[0].length == 1) ? 0 : binarySearch(rowValue, 'column');
    columnValue = columnValue < 0 ? 0 : columnValue;

    return target == matrix[rowValue][columnValue];
};
