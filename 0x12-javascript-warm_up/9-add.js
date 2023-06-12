#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const argInit = process.argv[2];
const argLast = process.argv[3];

const result = add(argInit, argLast);
console.log(result);
