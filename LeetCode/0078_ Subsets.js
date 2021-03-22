/*
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
*/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {

    let result = [[]];
    let subset = [];

    for (let limit = 1; limit <= nums.length; limit++) {

        let generator = function (startNumber) {
            if (subset.length == limit) {
                result.push(Array.from(subset));
                return;
            }
            for (let i = startNumber; i < nums.length; i++) {
                subset.push(nums[i]);
                generator(i + 1);
                subset.pop();
            }
        }

        generator(0);
    }

    return result;
};
