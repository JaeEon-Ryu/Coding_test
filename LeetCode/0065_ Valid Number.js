/*
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], 
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
*/

/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function (s) {

    // reference : antipin

    s = s.trim()
    let arr = [];

    function helper(str, isInt) {

        let dotCount = 0
        let digitCount = 0
        let startIndex = (str[0] === '-' || str[0] === '+') ? 1 : 0

        for (let i = startIndex; i < str.length; ++i) {
            if (str[i] === '.') dotCount++
            if (str[i] >= '0' && str[i] <= '9') digitCount++
            if ((str[i] < '0' || str[i] > '9') && str[i] !== '.') return false
        }

        return digitCount > 0 && ((isInt && dotCount === 0) || (!isInt && dotCount <= 1))
    }

    if (s.includes('e') || s.includes('E')) {
        let sub_arr = '';

        for (let sub_s of s) { // s.split('e')으로 대체 가능
            if (sub_s == 'e' || sub_s == 'E') {
                arr.push(sub_arr)
                sub_arr = '';
            }
            else {
                sub_arr += sub_s
            }
        }
        arr.push(sub_arr)

        if (arr.length != 2 || arr[0] == '' || arr[1] == '') {
            return false
        }
        else {
            return helper(arr[0]) && helper(arr[1], true)
        }

    }
    else {
        return helper(s)
    }


};
