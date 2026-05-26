

arr = [2, 5,5, 8,12, 12, 16, 23, 28, 33, 45, 52, 60, 71, 88]


function lowerBound(arr , target) {
    
    let n = arr.length-1;
    let l =0 ,h = n;
    let ans =-1;

    while (l <= h) {
        
        let mid = Math.floor((l + h)/2);
        if( arr [ mid] >= target){
            ans = mid
            h = mid-1;
        }else {
            l = mid+1
        }
    }
    return ans
}

let target =5;
console.log("first appearence of the target",{target}," is " , lowerBound(arr , target))