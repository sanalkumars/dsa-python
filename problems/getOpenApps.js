// question description

// getOpenApplications

// Editable code area with the corrected solution
// 5 automated test cases with pass/fail badges
// A custom input box — type any commands (one per line) and it shows you the stack state after every single command


// solution

const getOpenApps =( commands)=>{

    //  creating stack ( since stack uses lifo)

    const stack =  [ ];

    for (let i = 0; i < commands.length; i++) {
        const cmd = commands[i].trim();

        if (cmd === "clear") {
            stack =[ ]; // this is for resetting the stack to empty
        }else if ( cmd.startsWith  === "open"){
            // in this case we push the new app
            let cmdname = cmd.splice(5);
            stack.push(cmdname)
        }else if ( cmd.startsWith === "close"){
            let numberofappstoclose = parseInt(cmd.splice(6))

            for (let j = 0; j < numberofappstoclose; j++) {
                if( stack.length >0 ) stack.pop()     // this removes the n/numnberofappstoclose number of apps from the top of the stack            
            }
        }
        
    }

    return stack
}