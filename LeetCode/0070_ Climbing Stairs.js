/*
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
*/

/**
 * @param {number} n
 * @return {number}
 */
// dp 활용
var climbStairs = function (n) {
    let stairs = [0, 1, 2];

    for (let i = 2; i <= n; i++) {
        stairs.push(stairs[i - 1] + stairs[i]);
    }

    return stairs[n];
};


/*
1 -> 1
2 -> 1, 2 -> 2
3 -> 1+1+1, 2+1, 1+2 -> 3
4 -> 1+1+1+1, 2+2, 1+2+1, 1+1+2, 2+1+1 -> 5
*/