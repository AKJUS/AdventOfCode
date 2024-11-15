// Advent of Code 2015 - Day 6

// Read Puzzle from day3.txt and save in puzzle variable
const fs = require("fs");
const txt = "day5.txt";
const readFile = function(txt){
  return fs.readFileSync(txt).toString();
};
var puzzle = readFile(txt);

// Solution 
