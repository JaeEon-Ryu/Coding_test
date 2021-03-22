/*
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.
*/

/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {

    let result = [];
    let combinations = [];

    let generator = function (startNumber) {
        if (combinations.length == k) {
            result.push(Array.from(combinations));
            return;
        }
        for (let i = startNumber; i <= n; i++) {
            combinations.push(i);
            generator(i + 1);
            combinations.pop();
        }
    }

    generator(1);
    return result;
};
