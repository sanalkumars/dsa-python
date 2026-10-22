

// leetcode 347

// technique is hashmap + sorting 

const topKfrequent = (nums)=>{

    let frequency = new Map();
    
    for( const num of nums){
        frequency.set( num , ( frequency.get(num) || 0 ) + 1);
    }
    const sortedKeys = [...frequency.keys()].sort((a,b) => frequency.get(b) - frequency.get(a));

    // return top  k element

    return sortedKeys.splice(0 , k)
}

let nums = [1,1,1,2,2,3];
let k = 2;

console.log("top k frequent element is ",topKfrequent(nums , k))