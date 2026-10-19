

function RemoveDup(nums){

    for( let i =0 ;i < nums.length-1 ; i++){
        if (nums[i] === nums[ i+1]) {
            nums.splice(i +1 ,1);
            i--;
        }
    }

    return nums.length;
}

let nums = [1,1,2,2,3,4,5,5];
let newLength = RemoveDup(nums);
console.log(nums);
console.log("Number of unique elements:", newLength);