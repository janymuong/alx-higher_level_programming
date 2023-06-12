#!/usr/bin/node

const arg = process.argv[2];

// log err if arg contains no value; else value;
const outVal = arg !== undefined ? arg : 'No argument';
console.log(outVal);
