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
    console.log(seenStr)
    return [ ...seenStr]
}

let substrings = findUniqueSubstrings("abac")
console.log("unique sub strings are ", substrings)