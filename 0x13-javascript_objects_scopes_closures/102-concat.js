#!/usr/bin/node

// concatenate file contents in command-line;
const fs = require('fs');

const readFileA = fs.readFileSync(process.argv[2], 'utf8');
const readFileB = fs.readFileSync(process.argv[3], 'utf8');
const concatContent = readFileA + readFileB;

fs.writeFileSync(process.argv[4], concatContent);
