/*
Given a rows x cols binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.
*/

/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function (matrix) {
    if (matrix.length == 0) return 0;

    rows = matrix.length;
    cols = matrix[0].length;
    maximalArea = 0;

    // Verify that all values in the zone are 1
    let areAllvaluesCorrect = function (sX, sY, eX, eY) { // startX,startY,endX,endY
        for (let x = sX; x <= eX; x++) {
            for (let y = sY; y <= eY; y++) {
                if (matrix[x][y] == "0") {
                    return false;
                }
            }
        }
        return true;
    };

    // Rectangular detection from existing coordinates
    let LargestRectangularDetection = function (startX, startY) {
        let maxValue = 0;

        for (let endX = startX; endX < rows; endX++) {
            for (let endY = startY; endY < cols; endY++) {
                if (matrix[endX][endY] == "0") {
                    break;
                }
                else {
                    if (areAllvaluesCorrect(startX, startY, endX, endY)) {
                        maxValue = Math.max(maxValue, (endX - startX + 1) * (endY - startY + 1));
                    }
                }
            }
        }
        return maxValue;
    };

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            maximalArea = Math.max(maximalArea, LargestRectangularDetection(i, j));
        }
    }

    return maximalArea;
};

