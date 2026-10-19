
// brute force approach ( this have o(nlogn) time complexity)
// function secondLargest( arr ) {

//     let uniqueArrset = new Set(arr); //this convert the array that contains duplicates in to a set
//     const uniqueArr = Array.from(uniqueArrset).sort((a,b)=> a-b) //converts the set in to an array then sort it in ascending order
//     if(uniqueArr.length >=2){
//         return uniqueArr[ uniqueArr.length-2]
//     }else{
//         return -1
//     }
// }

// let secondLarget = secondLargest([ 1,5,4,1,2,6,5,12,2,4,11])
// console.log("second larget element is ",secondLarget)

// Optimised version (this version have o(n) time complexity)
function optimisedVersion(arr) {
    let l = Number.NEGATIVE_INFINITY;
    let secondL = Number.NEGATIVE_INFINITY;
    if( arr.length < 2) return
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > l ) {
            secondL = l
            l = arr[i];
        }else if( arr[i] < l && arr[i] > secondL ){
            secondL = arr[i]
        }     
    }
    return secondL;
}

const secondLargest = optimisedVersion([1,2,5,4,6,1,5,9,8,10])

console.log("second largest element is ",secondLargest)