// Advent of Code 2015 - Day 4

// Import MD5 Hash library
var md5 = require('js-md5');

// Solution
let hashFound = false;
let hashNumber = 0;
let hashPhrase = "yzbqklnj";

// Alter code depending on Part 1 / 2 
// Part 1 -> result.slice(0, 5) and check against "00000"
// Part 2 -> result.slice(0. 6) and check against "000000"
while(hashFound != true){
  let hashTest = hashPhrase + hashNumber;
  let result = md5(hashTest);
  let checkForZero = result.slice(0, 6);
  if(checkForZero == "000000"){
    console.log("The lowest number to get 5 x 0 is:", hashNumber);
    hashFound = true;
  }else{
    hashNumber++;
  }
};
