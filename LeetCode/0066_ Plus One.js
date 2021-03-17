/*
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
*/

var plusOne = function (digits) {

    for (let i = digits.length - 1; i >= 0; i--) {
        if (digits[i] == 9) {
            digits[i] = 0;
            if (i == 0) {
                digits.unshift(1)
            }
        }
        else {
            digits[i] += 1;
            break
        }
    }

    return digits

    /*
    이렇게 하면 숫자 길이가 길어질경우 오류 발생
    num = '';
    for (let n of digits) {
        num += String(n)
    }
    num = String(Number(num) + 1)

    result = [];
    for (let s of num) {
        result.push(Number(s))
    }

    console.log(result)
    return result
    */
};

plusOne([4, 3, 2, 1])