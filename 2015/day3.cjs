// Advent of Code 2015 - Day 3

// Read Puzzle from day3.txt and save in puzzle variable
const fs = require("fs");
const txt = "day3.txt";
const readFile = function(txt){
  return fs.readFileSync(txt).toString();
};
var puzzle = readFile(txt);

// Solution
let x = 0;
let y = 0;
let visitedHouses = ["0x0y"];


// Visit every house Part 1
for (i = 0; i < puzzle.length; i++){
  if(puzzle[i] == "<"){
    x = x - 1;}
  else if(puzzle[i] == ">"){
    x = x + 1;  }
  else if(puzzle[i] == "v"){
    y = y - 1;  }
  else{
    y = y + 1;  }
  let coordinate = x.toString()+"x"+y.toString()+"y";
  visitedHouses.push(coordinate);
};

// Find houses visited at least once Part 1
let sortedVisits = visitedHouses.sort();
let atLeastOne = 1;
for(i = 0; i < sortedVisits.length - 1; i++){
  if(sortedVisits[i] != sortedVisits[i + 1]){
    atLeastOne++;
  }
};

// Santa and Robot take turns in visiting Part 2 
let changeOver = 0;
let visitedHousesSanta = ["0x0y"];
let visitedHousesRobo = ["0x0y"];
let xSanta = 0;
let ySanta = 0;
let xRobo = 0;
let yRobo = 0;
for (i = 0; i < puzzle.length; i++){
  if(puzzle[i] == "<"){
    if(changeOver%2 == 0){
      xSanta = xSanta - 1;
    }
    else{
      xRobo = xRobo - 1;
    }
  }
  else if(puzzle[i] == ">"){
    if(changeOver%2 == 0){
      xSanta = xSanta + 1;
    }
    else{
      xRobo = xRobo + 1;
    }
  }
  else if(puzzle[i] == "v"){
    if(changeOver%2 == 0){
      ySanta = ySanta - 1;
    }
    else{
      yRobo = yRobo - 1;
    }
  }
  else{
    if(changeOver%2 == 0){
      ySanta = ySanta + 1;
    }
    else{
      yRobo = yRobo + 1;
    }
  }
  if(changeOver%2 == 0){
    let coordinateSanta = xSanta.toString()+"x"+ySanta.toString()+"y";
    visitedHousesSanta.push(coordinateSanta);
  }
  else{
    let coordinateRobo = xRobo.toString()+"x"+yRobo.toString()+"y";
    visitedHousesRobo.push(coordinateRobo);
  }
  changeOver++;
};

// Houses visited by Santa or Robo at least once Part 2
let mergedList = visitedHousesRobo.concat(visitedHousesSanta);
let sortedMergedList = mergedList.sort();

let atLeastOneNew = 1;
for(i = 0; i < sortedMergedList.length - 1; i++){
  if(sortedMergedList[i] != sortedMergedList[i + 1]){
    atLeastOneNew++;
  }
};

console.log("Santa houses visited at least once:", atLeastOne);
console.log("Santa & Robot visited at least once:", atLeastOneNew);
