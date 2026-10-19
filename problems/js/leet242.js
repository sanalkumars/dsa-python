// valid anagram

// solution : we can create a map and count the frequency of each element of first string , the we reduce the frequency in the map based on the second map


const isValidAnagram = ( s , t)=>{

    if( s.length !== t.length) return false;

    let freq = new Map();
    // first string frequency counting 
    for( const str of s ){
        freq.set(str , ( freq.get(str)|| 0) + 1)
    }

    for (const str of t) {
        if( !freq.has(str)) return false
        let count = freq.get(str);
        if ( count ===1) {
            freq.delete(str)
        }else{
            freq.set( str , count - 1)
        }
    }

    // once out of the loop we check if the freq size is 0 then it means both string are valid anagram 
    return freq.size === 0

}
s = "anagram"
t = "nagaram"

console.log("is valid anagram: " , isValidAnagram(s,t))