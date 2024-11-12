// Advent of Code 2015 - Day 5 

// Read Puzzle from day3.txt and save in puzzle variable
const fs = require("fs");
const txt = "day5.txt";
const readFile = function(txt){
  return fs.readFileSync(txt).toString();
};
var puzzle = readFile(txt);

// Solution 
let niceWordsPart1 = 0;
let niceWordsPart2 = 0;
let words = puzzle.split("\n");

for(i = 0; i < words.length; i++){
  let vowels = 0;
  let doubler = 0;
  let naughty = false;
  let doubleApperance = 0;
  let inBetween = 0;
  let inBetweenFound = false;
  // Part 1

  // Check for vowels and count
  for(x = 0; x < words[i].length; x++){
    if(words[i][x] == "a"){
      vowels++;
    }else if(words[i][x] == "e"){
      vowels++;
    }else if(words[i][x] == "i"){
      vowels++;
    }else if(words[i][x] == "o"){
      vowels++;
    }else if(words[i][x] == "u"){
      vowels++;
    }
  }

  // Check for doublers
  for(x = 0; x < words[i].length; x++){
    if(words[i][x] == words[i][x + 1]){
      doubler++;
    }
  }

  // Check for naughty 
  if(words[i].includes("ab") || words[i].includes("cd") || words[i].includes("pq") || words[i].includes("xy")){
    naughty = true;
  }

  // Get Result
  if(vowels >= 3 && doubler >= 1 && naughty != true){
    niceWordsPart1++;
  }

  // Part 2 
  // Check for double appearance without overflow


  // Check for same letter with different letter in between 

};


console.log("Nice words found for Part 1:", niceWordsPart1);
console.log("Nice words found for Part 2:", niceWordsPart2);
