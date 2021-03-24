/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {

    let currentNum = 0;
    let currentCnt = 0;
    let i = 0; // index

    while (i < nums.length) {
        if (currentNum != nums[i]) { // 기존값과 다를 때
            if (currentCnt > 2) {
                nums.splice(i - currentCnt, currentCnt - 2);
                i -= (currentCnt - 2);
            }
            currentNum = nums[i];
            currentCnt = 1;
        }
        else {
            currentCnt++;
        }
        i++;
    }
    if (currentCnt > 2) { // 마지막 값이 검사되지 않았을 경우
        nums.splice(nums.length - currentCnt, currentCnt - 2);
    }

    return nums.length;
};

removeDuplicates([0, 0, 1, 1, 1, 1, 2, 2, 2, 4]);