#!/usr/bin/node

const { dict } = require('./101-data');

const sortDict = {};
for (const userId in dict) {
  const occurrence = dict[userId];
  if (occurrence in sortDict) {
    sortDict[occurrence].push(userId.toString());
  } else {
    sortDict[occurrence] = [userId.toString()];
  }
}

console.log(sortDict);
