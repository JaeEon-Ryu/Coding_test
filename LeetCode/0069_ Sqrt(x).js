/*
Given a non-negative integer x, 
compute and return the square root of x.

Since the return type is an integer, 
the decimal digits are truncated, 
and only the integer part of the result is returned. */

/**
 * @param {number} x
 * @return {number}
 */
// 이분탐색 활용
var mySqrt = function (x) {

    var left = 0;
    var right = x;

    while (!(mid ** 2 <= x && x < (mid + 1) ** 2)) {
        var mid = parseInt((left + right) / 2);

        if (mid ** 2 < x) {
            left = mid + 1;
        }
        else if (mid ** 2 > x) {
            right = mid;
        }

    }

    return mid;
};