

function LongestUniqueSubstring(s){

    let seen = new Map();
    let left =0;
    let maxLnth = 0;
    let maxStr ="";

    for ( let r =0; r < s.length;r++){
        let char = s[r];

        if (seen.has(char) && seen.get(char) >= left) {
            left = seen.get(char) + 1
            
        }

        seen.set(char ,r);

        if (r-left +1 > maxLnth) {
            maxLnth = r-left+1;
            maxStr = s.slice(left , r+1)
        }
    }

    return { maxLnth , maxStr}
}

const {  maxLnth , maxStr} = LongestUniqueSubstring("abacd")
console.log("maxlength for unique string",maxLnth)
console.log("longest unique string",maxStr)