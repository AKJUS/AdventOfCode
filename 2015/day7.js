// Advent of Code 2015 - Day 7

// Read Puzzle from day7.txt and save in puzzle variable
const fs = require("fs");
const txt = "day7.txt";
const readFile = function(txt){
  return fs.readFileSync(txt).toString();
};
let puzzle = readFile(txt).split("\n");

// Clean up instructions
let instructions = [];
for(ins = 0; ins < puzzle.length; ins++){
  instructions.push(puzzle[ins].split(" "));
};
console.log(instructions);

// Bitwise operations
// https://en.wikipedia.org/wiki/Bitwise_operation
