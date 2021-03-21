/*
Given two strings s and t, 
return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, 
return the empty string "".

Note that If there is such a window, 
it is guaranteed that there will always be only one unique minimum window in s.
*/

/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {

    // reference : AminiCK

    let min = "", left = 0, right = -1;
    let map = {};

    // 알파벳을 카운트 함으로써 수행시간을 줄일 수 있음
    t.split('').forEach(element => {
        if (map[element] == null) map[element] = 1;
        else map[element] = map[element] + 1;
    });

    let count = Object.keys(map).length;

    while (right <= s.length) {

        if (count == 0) {
            let current = s[left];

            if (map[current] != null) map[current]++;
            if (map[current] > 0) count++;

            let temp = s.substring(left, right + 1)
            if (min == "") min = temp;
            else min = min.length < temp.length ? min : temp;

            left++;

        } else {
            right++;
            let current = s[right];

            if (map[current] != null) map[current]--;
            if (map[current] == 0) count--;
        }
    }
    return min;

    /*
    시간초과가 났던 코드
    let result = s;

    function isInTheSentence(sentence1, sentence2) {
        for (let word2 of sentence2) {
            if (sentence1.includes(word2)) {
                sentence1 = sentence1.replace(word2, '');
            }
            else {
                return false;
            }
        }
        return true;
    }

    let left = 0, right = 0;
    while (right < s.length) {
        slicedS = s.slice(left, right + 1);

        if (isInTheSentence(slicedS, t)) {
            if (slicedS.length < result.length) {
                result = slicedS;
            }
            left++;
        }
        else {
            right++;
        }
    }

    if (result == "thereIsNoSuchWindow") {
        return ""
    }
    else {
        return result;
    }

    */

};
