
// valid palindrome


// brute force approach - time complexity O(n^2) , space complexity O(n)

const isValidPalindromeBrute = (s)=>{

    // remove non-alphanumeric characters and convert to lower case

    const cleaned = s.replace(/[^a-z0-9]/gi,"").toLowerCase();


    // reverse the coverted
    const reversed = cleaned.split("").reverse().join("");

    // compare both converted and reversed

    return reversed === cleaned;
}

console.log("is valid palindrome:",isValidPalindromeBrute(s="A man, a plan, a canal: Panama"))