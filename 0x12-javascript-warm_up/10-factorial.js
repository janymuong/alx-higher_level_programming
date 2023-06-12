#!/usr/bin/node

const factorial = (argInt) => {
  if (isNaN(argInt)) {
    return 1;
  }

  if (argInt === 0 || argInt === 1) {
    return 1;
  }

  return argInt * factorial(argInt - 1);
};

const argInt = parseInt(process.argv[2]);
const result = factorial(argInt);
console.log(result);
