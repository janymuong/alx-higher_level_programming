#!/usr/bin/node

// concatenate args to string literal
const argInit = process.argv[2];
const argFinal = process.argv[3];

console.log(`${argInit} is ${argFinal}`);
