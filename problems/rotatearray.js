nums = [1,2,3,4,5,6,7,8,9]

function rotateArray(arr, k) {
    k = k % arr.length;

    return arr.splice(arr.length-k).concat(arr);
}

const rotatedArray = rotateArray(nums, 4);
console.log(rotatedArray);