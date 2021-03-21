/*
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

!! solve this problem without using the library's sort function !! 
!! come up with a one-pass algorithm using only O(1) constant space !!
*/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {

    let cntRed = 0, cntWhite = 0, cntBlue = 0;

    for (let num of nums) {
        if (num == 0) {
            cntRed++;
        }
        else if (num == 1) {
            cntWhite++;
        }
    }

    cntBlue = nums.length - cntWhite - cntRed;
    nums.length = 0;

    for (let i = 0; i < cntRed; i++) {
        nums.push(0);
    }
    for (let i = 0; i < cntWhite; i++) {
        nums.push(1);
    }
    for (let i = 0; i < cntBlue; i++) {
        nums.push(2);
    }

};
