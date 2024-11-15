// Advent of Code 2015 - Day 6

// Read Puzzle from day6.txt and save in puzzle variable
const fs = require("fs");
const txt = "day6.txt";
const readFile = function(txt){
  return fs.readFileSync(txt).toString();
};
var puzzle = readFile(txt);

// Test for Grid
// Each index in testGrid = x coordinate and is filled with y coordinates
// and state of light
let testGrid = [];
for(x = 0; x < 5; x++){
  let yCoor = [];
  for(y = 0; y < 5; y++){
    yCoor.push({y, state:0})
  }
  testGrid.push(yCoor);
};

// Tests
let testCommands = ["toggle 2,1 through 4,2"];

for(command = 0; command < testCommands.length; command ++){
  let instruction = testCommands[command].split(" ");
  let xRange = [];
  let yRange = [];
  xRange.push(instruction[1].split(",")[0]);
  xRange.push(instruction[3].split(",")[0]);
  yRange.push(instruction[1].split(",")[1]);
  yRange.push(instruction[3].split(",")[1]);
  console.log(xRange, yRange);
}

//console.table(testGrid);
