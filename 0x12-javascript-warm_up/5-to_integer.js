#!/usr/bin/node

const arg = process.argv[2];
const argInt = parseInt(arg);

// log (int) converted number or err
const outVal = isNaN(argInt) ? 'Not a number' : `My number: ${argInt}`;
console.log(outVal);
