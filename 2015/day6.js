// Advent of Code 2015 - Day 6

// Read Puzzle from day6.txt and save in puzzle variable
const fs = require("fs");
const txt = "day6.txt";
const readFile = function(txt){
  return fs.readFileSync(txt).toString();
};
let puzzle = readFile(txt).split("\n");

// Clean up puzzle instructions
let instructions = [];
for(let ins = 0; ins < puzzle.length - 1; ins++){
  let buffer = [];
  let temp = puzzle[ins].split(" ");
  if(temp[0] == "turn"){
    buffer.push(temp[1]);
    buffer.push(temp[2].split(","));
    buffer.push(temp[4].split(","));
  }else{
    buffer.push(temp[0]);
    buffer.push(temp[1].split(","));
    buffer.push(temp[3].split(","));
  }
  // Change x and y coordinate from str to int 
  buffer[1][0] = parseInt(buffer[1][0]);
  buffer[1][1] = parseInt(buffer[1][1]);
  buffer[2][0] = parseInt(buffer[2][0]);
  buffer[2][1] = parseInt(buffer[2][1]);
  instructions.push(buffer);
}

// Create Grid of Lights
let lightGrid = [];
for(let gridX = 0; gridX < 10; gridX++){
  let tempoRow = [];
  for(let gridY = 0; gridY < 10; gridY++){
    tempoRow.push([0]);
  }
  lightGrid.push(tempoRow);
}

lightGrid[1][1] = [1];
console.table(lightGrid); 
