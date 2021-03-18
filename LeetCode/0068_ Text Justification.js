/*Given an array of words and a width maxWidth, 
format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; 
that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words. */

/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */

var fullJustify = function (words, maxWidth) {

    // 배열에 있는 단어 길이들의 합
    var wordsLen = function (subWords) {
        lenSum = 0;
        for (var word of subWords) {
            lenSum += word.length;
        }

        return lenSum;
    };

    // 한 줄에 표기 할 문장 작성 ( tempWords = 문장, last = 마지막 문장인지 아닌지 )
    var sentenceGenerator = function (tempWords, last) {
        var sentence = '';
        var spaceNum = maxWidth - wordsLen(tempWords);
        var reminder = spaceNum % (tempWords.length - 1); // 나누어 떨어지지 않은 것 대비
        var repeat = parseInt(spaceNum / (tempWords.length - 1)); // repeat만큼 공백 추가

        // 마지막 문장이라면 공백 수정
        if (last) {
            repeat = 1;
            reminder = 0;
        }

        sentence += tempWords[0];
        for (var i = 1; i < tempWords.length; i++) {
            for (var _ = 0; _ < repeat; _++) {
                sentence += ' ';
            }
            if (reminder) {
                sentence += ' ';
                reminder -= 1;
            }
            sentence += tempWords[i];
        }

        // 맨 마지막 문장에 대한 추가 코드 ( 공백을 끝까지 두게하기 위함 )
        if (sentence.length != maxWidth) {
            while (sentence.length != maxWidth) {
                sentence += " ";
            }
        }

        return sentence;
    };

    let i = 0;
    let temp = [];
    let result = [];

    while (i < words.length) {
        temp.push(words[i]);
        if (wordsLen(temp) + temp.length - 1 > maxWidth) {
            temp.pop();
            result.push(sentenceGenerator(temp, false));
            temp = [];
        }
        else {
            i += 1;
        }
    }
    if (temp) { // 마지막 문장 결합
        result.push(sentenceGenerator(temp, true));
    }

    return result;

};

