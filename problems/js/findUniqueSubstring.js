// WE will use Set to get the unique substrings , Set only stores unique values
// so no need to do any extra condition or check

function findUniqueSubstrings(s) {

    let seenStr = new Set(); // this returns an object { } not a array  , so finally we need to 
    // convert this to an array using [...](spred operator)

    for (let i = 0; i < s.length; i++) {
        for (let j = i+1; j <= s.length; j++) {
            seenStr.add(s.slice(i,j))        
        }
        
    }
    // console.log(seenStr)
    // if u want to return the number of unique substrings
    return {substrs :[ ...seenStr] , count :seenStr.size}
}

let {substrs , count} = findUniqueSubstrings("abac")
console.log("unique sub strings are ", substrs)
console.log("total unique sub strings are ", count)