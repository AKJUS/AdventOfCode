// Advent of Code 2015 - Day 2

// Read Puzzle from day2.txt and save in puzzle variable
const fs = require("fs");
const txt = "day2.txt";
const readFile = function(txt){
  return fs.readFileSync(txt).toString();
};
var puzzle = readFile(txt);

// Solution 
var packages = puzzle.split("\n");
var total = 0;
var ribbonTotal = 0;
for(i = 0; i < packages.length-1; i++){
  // Part 1
  var present = packages[i].split("x");
  let sides = [];
  let smallest = [];
  var l = present[0];
  var w = present[1];
  var h = present[2];
  // calculate paper for package
  sides.push(2*l*w);
  sides.push(2*w*h);
  sides.push(2*h*l);
  // calculate smallest side
  smallest.push(l*w);
  smallest.push(w*h);
  smallest.push(h*l);
  // sort for smallest side first
  let smallestFirst = smallest.sort((a, b) => a - b);
  // add all sides plus smallest
  total = total + sides[0] + sides[1] + sides[2] + smallestFirst[0];

  // Part 2
  let ribbonSides = [];
  ribbonSides.push(l);
  ribbonSides.push(w);
  ribbonSides.push(h);
  let sortedSides = ribbonSides.sort((a, b) => a - b);
  ribbonTotal = ribbonTotal + parseInt(sortedSides[0])*2 + parseInt(sortedSides[1])*2 +
  (parseInt(sortedSides[0])*parseInt(sortedSides[1])*parseInt(sortedSides[2]));
  
};

console.log("Sqaure feet needed by elfes:", total);
console.log("Length of ribbon needed by elfes:", ribbonTotal);
