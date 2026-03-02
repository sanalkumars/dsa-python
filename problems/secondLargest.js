
// brute force approach
function secondLargest( arr ) {

    let uniqueArrset = new Set(arr); //this convert the array that contains duplicates in to a set
    const uniqueArr = Array.from(uniqueArrset).sort((a,b)=> a-b) //converts the set in to an array then sort it in ascending order
    if(uniqueArr.length >=2){
        return uniqueArr[ uniqueArr.length-2]
    }else{
        return -1
    }
}

let secondLarget = secondLargest([ 1,5,4,1,2,6,5,12,2,4,11])
console.log("second larget element is ",secondLarget)