# ![title](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3jOK2wxE5meq4Qn32Z8I7BassGI5BwB6rhQ&s)Advent of Code 

## Motivation
I started Advent of Code because I had a little motivational drop while doing the last part of the Meta Front End Certificate on Coursera.
Since AoC goes back all the way to 2015, I figured it would keep me busy for a while and give me a nice challenge.

## Cool Tricks I found
To check how often a string or character appears in a given string, I stumbled upon a nice simple way to do this in JavaScript
```JavaScript
let target = "ab";
let text = "jlksdfabjsöldjfösdabkdsjfösdlfjab";
let count = text.split(target).length -1;
```

This spilts the string in x peaces when it removes the searched for string. If found once, there will be two new strings, therefore the -1 
***
