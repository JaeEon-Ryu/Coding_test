/*
Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest rectangle in the histogram.
*/

/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function (heights) {

    // reference : HarikiRito
    let maxArea = 0;
    const stack = [];
    heights = [0].concat(heights).concat([0]);

    for (let i = 0; i < heights.length; i++) {
        while (stack && heights[stack[stack.length - 1]] > heights[i]) {
            const j = stack.pop();
            console.log(stack[stack.length - 1], heights[j]);
            maxArea = Math.max((i - stack[stack.length - 1] - 1) * heights[j], maxArea);
        }
        stack.push(i);
    }

    return maxArea;

    // let l = 0;
    // let r = heights.length - 1;
    // largestArea = 0;
    // while (l <= r) {
    //     largestArea = Math.max(largestArea, (r - l + 1) * Math.min.apply(null, heights));
    //     if (heights[0] >= heights[heights.length - 1]) {
    //         heights.splice(-1);
    //         r--;
    //     }
    //     else {
    //         heights.splice(0, 1);
    //         l++;
    //     }
    // }
    // console.log(largestArea)
    // return largestArea;
};

//[4, 2, 0, 3, 2, 4, 3, 4]
largestRectangleArea([2, 1, 5, 6, 2, 3]);