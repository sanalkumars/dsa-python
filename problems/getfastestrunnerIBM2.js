// Problem2 from IBM 

// Find the runner with the highest top_speed for a given marathon name and sex. 
// Fetch paginated data
//  from https://jsonmock.hackerrank.com/api/marathon?sex=<sex>&page=<n>. Return the runner's name as a string.


async function findSpeedster(marathon , sex) {

    let page =1
    let topSpeed = -Infinity;
    let speedster ='';

    while (true) {
        
        const url = `https://jsonmock.hackerrank.com/api/marathon?sex=${sex}&page=${page}`
    
        const response = await fetch(url);
    
        const data = await response.json()
    
        for( const runner in data.data){
            if ( runner.marathon_name === marathon && runner.top_speed > topSpeed) {
                topSpeed = runner.top_speed;
                speedster = runner.name 
            }
        }

        if (page >= data.total_page) {
            break
        }
        page ++ ;
    }

    return speedster;
    
}
