// Contains Duplicate

// brute force , we can compare each element with remaining elements which will leads to O(n^2)


// optimal solution using a 'set'

const hasDuplicate = ( nums )=>{
    let seen = new Set()
    for ( const num of nums){

        if (seen.has(num)) {
            return true
        }
            seen.add(num)
        
    }
    return false;
}

let nums = [1, 2, 3, 1]    // output : true
let nums2 = [1, 2, 3, 4]    // output : false

console.log("has duplicate:",hasDuplicate(nums))