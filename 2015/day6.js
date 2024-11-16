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
  if(raw[1] == "off" || raw[1] == "on"){
    toDo.push(raw[1]);
    toDo.push(raw[2].split(","));
    toDo.push(raw[4].split(","));
  }else{
    toDo.push(raw[0]);
    toDo.push(raw[1].split(","));
    toDo.push(raw[3].split(","));
  }
  return toDo;
};


// cycle through grid and perform actions
for(instr = 0; instr < puzzle.length-1; instr++){
  let command = getInstructions(puzzle[instr]);
  // comand is [instruction, [xStart, yStart], [xEnd, yEnd]]
  //                 [0]      [1][0]  [1][1]  [2][0]  [2][1]

  // First non complete row
  for(firstRow = parseInt(command[1][1]); firstRow < 1000; firstRow++){
    if(command[0] == "toggle"){
      if(lightGrid[parseInt(command[1][0])][firstRow].state == 1){
        lightGrid[parseInt(command[1][0])][firstRow].state = 0;
      }else{
        lightGrid[parseInt(command[1][0])][firstRow].state = 1;
      }
    }else if(command[0] == "on"){
      lightGrid[parseInt(command[1][0])][firstRow].state = 1;
    }else if(command[0] == "off"){
      lightGrid[parseInt(command[1][0])][firstRow].state = 0;
    }
  }

  // All complete rows
  for(row = parseInt(command[1][0])+1; row < parseInt(command[2][0]); row++){
    for(col = 0; col < 1000; col++){
      if(command[0] == "toggle"){
        if(lightGrid[row][col].state == 1){
          lightGrid[row][col].state = 0;
        }else{
          lightGrid[row][col].state = 1;
        }
      }else if(command[0] == "on"){
        lightGrid[row][col].state = 1;
      }else if(command[0] == "off"){
        lightGrid[row][col].state = 0;
      }
    }
  }

  // Last non complete row 
  for(lastRow = 0; lastRow <= parseInt(command[2][1]); lastRow++){
    if(command[0] == "toggle"){
      if(lightGrid[parseInt(command[2][0])][lastRow].state == 1){
        lightGrid[parseInt(command[2][0])][lastRow].state = 0;
      }else{
        lightGrid[parseInt(command[2][0])][lastRow].state = 1;
      }
    }else if(command[0] == "on"){
      lightGrid[parseInt(command[2][0])][lastRow].state == 1;
    }else if(command[0] == "off"){
      lightGrid[parseInt(command[2][0])][lastRow].state == 0;
    }
  }
};

// Look for on lights
let count = 0;
for(row = 0; row < 1000; row++){
  for(col = 0; col < 1000; col++){
    if(lightGrid[row][col].state == 1){
      count++;      
    }
  }
};
console.log(count);
