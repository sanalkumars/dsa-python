nums = [1,2,3,4,5]

function rotateArray(arr, k) {
    k = k % arr.length;

    return arr.splice(arr.length-k).concat(arr);
}

// const rotatedArray = rotateArray(nums, 4);
// console.log(rotatedArray);


// solution second approach

function rotateArray2(nums , k){
    let s =  nums.length;
    if( k > s) k = k % s;

    reverseArr(nums , 0 , s-1);
    reverseArr(nums , 0 , k-1);
    reverseArr(nums , k , s-1);

    return nums;
}


console.log("rotated array is ", rotateArray2(nums , 3))




function reverseArr( nums , left , right ){

    while ( left < right){
        let temp = nums[left];
        nums[left++] = nums[right];
        nums[right--] = temp;
    }
}