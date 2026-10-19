

function findSubstring( str ){
    let res =[];

    for (let i = 0; i < str.length; i++) {
        for (let j = i +1; j <= str.length; j++) {
            res.push(str.slice(i,j))
            
        }        
    }
    console.log("substring are ",res)
}

findSubstring("abac")