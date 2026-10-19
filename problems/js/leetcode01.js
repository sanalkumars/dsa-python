
// problem - Two sum
let nums = [2, 7, 11, 15]
let target = 9

// solution


const twoSum = ( nums , target )=>{

    let seen = new Map();

    for (let i = 0; i < nums.length; i++) {
        
        let c = target - nums[i];

        if( seen.has(c)){
            return [ seen.get(c) , i]
        }else{
            seen.set(nums[i] , i)
        }
        
    }
}

console.log("two sum result:",twoSum(nums , target))