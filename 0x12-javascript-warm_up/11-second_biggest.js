#!/usr/bin/node

// rm first two elements from process.argv
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0); // If no argument or only one argument is passed, print 0
} else {
  const secondBiggest = args
    .map(Number)
    // sort the numbers and get the second element
    .sort((a, b) => b - a)[1];
  console.log(secondBiggest);
}
