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

// Create Grid of Lights for Part 1
let lightGrid = [];
for(let gridX = 0; gridX < 1000; gridX++){
  let tempoRow = [];
  for(let gridY = 0; gridY < 1000; gridY++){
    tempoRow.push(0);
  }
  lightGrid.push(tempoRow);
};

// Create Grid of Lights for Part 2 
let brightnessGrid = [];
for(let brightX = 0; brightX < 1000; brightX++){
  let tempoBright = [];
  for(let brightY = 0; brightY < 1000; brightY++){
    tempoBright.push(0)
  }
  brightnessGrid.push(tempoBright);
};

// Execute instruction

for(ins = 0; ins < instructions.length; ins++){

  // Store Instruction Details
  let action = instructions[ins][0];
  let xStart = instructions[ins][1][0];
  let xEnd = instructions[ins][2][0];
  let yStart = instructions[ins][1][1];
  let yEnd = instructions[ins][2][1];

  // Execute Instructions Part 1
  for(xRow = xStart; xRow <= xEnd; xRow++){
    for(yCol = yStart; yCol <= yEnd; yCol++){
      if(action == "toggle"){
        if(lightGrid[xRow][yCol] == 0){
          lightGrid[xRow][yCol] = 1;
        }else{
          lightGrid[xRow][yCol] = 0;
        }
      }else if(action == "on"){
        lightGrid[xRow][yCol] = 1;
      }else if(action == "off"){
        lightGrid[xRow][yCol] = 0;
      }else{
        console.log("Oops something went wrong at", xRow, yCol);
      }
    }
  }

  // Execute Instructions Part 2 
  for(xRow = xStart; xRow <= xEnd; xRow++){
    for(yCol = yStart; yCol <= yEnd; yCol++){
      if(action == "toggle"){
        brightnessGrid[xRow][yCol] = brightnessGrid[xRow][yCol] + 2;
      }else if(action == "on"){
        brightnessGrid[xRow][yCol] = brightnessGrid[xRow][yCol] + 1;
      }else if(action == "off"){
        if(brightnessGrid[xRow][yCol] > 0){
          brightnessGrid[xRow][yCol] = brightnessGrid[xRow][yCol] - 1;
        }
      }else{
        console.log("Oops something went wrong at", xRow, yCol);
      }
    }
  }


 }

// Count how many lights are on
let countLights = 0;
for(countX = 0; countX < 1000; countX++){
  for(countY = 0; countY < 1000; countY++){
    if(lightGrid[countX][countY] == 1){
      countLights++;
    }
  }
}

// Count total brightness 
let totalBrightness = 0;
for(row = 0; row < 1000; row++){
  for(col = 0; col < 1000; col++){
    totalBrightness = totalBrightness + brightnessGrid[row][col];
  }
}


console.log(countLights, "Lights are On");
console.log("Total Brightness is", totalBrightness);
