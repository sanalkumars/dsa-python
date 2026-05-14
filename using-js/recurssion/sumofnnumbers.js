

function sumOfNnumbers(n){

    if( n==1){
        return 1;
    }       

    return n + sumOfNnumbers(n-1);
}

console.log(sumOfNnumbers(10)) 