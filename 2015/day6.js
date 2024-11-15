// Advent of Code 2015 - Day 6

// Read Puzzle from day6.txt and save in puzzle variable
const fs = require("fs");
const txt = "day6.txt";
const readFile = function(txt){
  return fs.readFileSync(txt).toString();
};
var puzzle = readFile(txt).split("\n");

// Create light grid 1000 x 1000
let lightGrid = [];
for(x = 0; x < 1000; x++){
  let yCoor = [];
  for(y = 0; y < 1000; y++){
    yCoor.push({y, state:0})
  }
  lightGrid.push(yCoor);
};

// get coordinates and action from instruction
function getInstructions(instruction) {
  let toDo = [];
  let raw = instruction.split(" ");
  toDo.push(raw[0]);
  toDo.push(raw[1].split(","));
  toDo.push(raw[3].split(","));
  return toDo;
}

// cycle through grid and perform actions
function executeInstruction(commands){
  // to do
}

//console.log(getInstructions(puzzle[0]));
console.log(lightGrid[6][50].state);
