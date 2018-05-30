// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) {
    let box = str.split('')
    let initialValue = {}
    let max = 0
    let maxChar = ''

    var reducer = function(item, count){
        if (item[count]){
            item[count] += 1
        } else {
            item[count] = 1
        }
        return item
    }

    var result = box.reduce(reducer, initialValue)

    for (let char in result){
        if (result[char] > max){
            max = result[char]
            maxChar = char
        }
    }
    return maxChar
}


module.exports = maxChar;
