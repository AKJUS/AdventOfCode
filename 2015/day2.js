// Advent of Code 2015 - Day 2

// Read Puzzle from day2.txt and save in puzzle variable
const fs = require("fs");
const txt = "day2.txt";
const readFile = function(txt){
  return fs.readFileSync(txt).toString();
};
var puzzle = readFile(txt);

console.log(puzzle);
