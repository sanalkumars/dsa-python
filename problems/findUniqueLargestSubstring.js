

function findUniqueLargestSubstring(s){

    let uniqueStr = new Set()
    let largestUniqueStr ="";
    let lengthOfLargestSubstring=0;

    for (let i = 0; i < s.length; i++) {
        for (let j = i+1; j <= s.length; j++) {
            let substr = s.slice(i,j);
            if (substr.length > lengthOfLargestSubstring) {
                largestUniqueStr = substr;
                lengthOfLargestSubstring = substr.length
            }
            uniqueStr.add(substr)
        }
        
    }

    return{
        largestUniqueStr ,
        lengthOfLargestSubstring
    }
}

const { largestUniqueStr , lengthOfLargestSubstring} = findUniqueLargestSubstring("abacd");
console.log("largestUniqueStr",largestUniqueStr)
console.log("lengthOfLargestSubstring",lengthOfLargestSubstring)