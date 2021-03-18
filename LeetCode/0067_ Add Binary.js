/*
Given two binary strings a and b, return their sum as a binary string.
*/

var addBinary = function (a, b) {

    let lenAB = Math.max(a.length, b.length);
    a = a.split("").map(o => o = parseInt(o));
    b = b.split("").map(o => o = parseInt(o));

    // a와b 둘 다 동등하게 길이 맞추기
    for (var i = a.length; i < lenAB; i++) {
        a.unshift(0);
    }
    for (var i = b.length; i < lenAB; i++) {
        b.unshift(0);
    }

    upDigit = 0;
    result = '';

    for (var i = lenAB - 1; i > -1; i--) {
        var curNum = a[i] + b[i] + upDigit;

        if (curNum > 1) {
            upDigit = 1;
        }
        else {
            upDigit = 0;
        }

        result = String(curNum % 2) + result;
    }

    if (upDigit) {
        result = '1' + result;
    }

    return result;

    /*
    아래 풀이법 : 숫자가 커지면 오버플로우 발생
    // var num = Number(a) + Number(b);
    // num = String(num).split("").reverse().map(o => o = parseInt(o));
    // let result = '';

    // for (var i = 0; i < num.length; i++) {
    //     if (num[i] > 1 && i + 1 < num.length) {
    //         num[i + 1] += 1;
    //     }
    //     result = String(num[i] % 2) + result;
    // }

    // if (num[num.length - 1] > 1) {
    //     result = '1' + result;
    // }

    // console.log(result);
    // return result
    */
};
