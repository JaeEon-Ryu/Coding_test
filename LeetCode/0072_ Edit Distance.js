/*
Given two strings word1 and word2, 
return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

horse, ros

0 1 2 3  
1 1 2 3
2 2 1
3 2
4
5

*/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function (word1, word2) {

    let x = word1.length + 1;
    let y = word2.length + 1;
    let dp = [];

    // Initialize to zero
    for (let j = 0; j < x; j++) {
        let subDp = [];
        for (let i = 0; i < y; i++) {
            subDp.push(0);
        }
        dp.push(subDp);
    }

    // Insert Initial Value
    for (let i = 0; i < y; i++) {
        dp[0][i] = i;
    }
    for (let i = 0; i < x; i++) {
        dp[i][0] = i;
    }

    for (let i = 1; i < x; i++) {
        for (let j = 1; j < y; j++) {
            digonalValue = 0;
            if (word1[i - 1] == word2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            }
            else {
                dp[i][j] = 1 + Math.min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                );
            }
        }
    }

    return dp[x - 1][y - 1];
};


