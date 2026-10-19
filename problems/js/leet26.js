let arr = [1,1,2,2,4,4,5,5,5];



function removeDup(arr) {
    let map = new Set();

    let i =0;
    while(i < arr.length){
        if (map.has(arr[i])) {
            i++;
        }else{
            map.add(arr[i])
            i++
        }
    }
    return [ ...map]
}

const  res = removeDup(arr)

console.log(res)