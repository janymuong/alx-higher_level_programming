#!/usr/bin/node

// cmd number conveted to int
const argInt = parseInt(process.argv[2]);
const logString = ['Missing number of occurrences', 'C is fun'];

if (isNaN(argInt)) {
  console.log(logString[0]);
} else {
  let count = 0;
  while (count < argInt) {
    console.log(logString[1]);
    count++;
  }
}
